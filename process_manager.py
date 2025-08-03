"""
Process Manager - Handles EA App/Origin process detection and termination
"""

import psutil
import time
import subprocess
import logging


class ProcessManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # EA process names to look for
        self.ea_process_names = [
            'EADesktop.exe',      # EA App
            'Origin.exe',         # Origin
            'OriginWebHelperService.exe',  # Origin web helper
            'OriginClientService.exe',     # Origin client service
            'EABackgroundService.exe',     # EA background service
            'EALaunchHelper.exe',          # EA launch helper
        ]
    
    def find_ea_processes(self):
        """Find all running EA-related processes"""
        running_processes = []
        
        try:
            for process in psutil.process_iter(['pid', 'name', 'exe']):
                try:
                    process_name = process.info['name']
                    if process_name and any(ea_name.lower() in process_name.lower() 
                                          for ea_name in self.ea_process_names):
                        running_processes.append({
                            'pid': process.info['pid'],
                            'name': process_name,
                            'exe': process.info['exe']
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    # Process may have terminated or we don't have access
                    continue
                    
        except Exception as e:
            self.logger.error(f"Error finding EA processes: {e}")
        
        return running_processes
    
    def terminate_ea_processes(self, timeout=30):
        """Terminate all EA-related processes gracefully"""
        processes_to_terminate = self.find_ea_processes()
        
        if not processes_to_terminate:
            self.logger.info("No EA processes found to terminate")
            return True
        
        self.logger.info(f"Attempting to terminate {len(processes_to_terminate)} EA processes")
        
        # First, try graceful termination
        terminated_pids = []
        for process_info in processes_to_terminate:
            try:
                process = psutil.Process(process_info['pid'])
                process.terminate()
                terminated_pids.append(process_info['pid'])
                self.logger.info(f"Sent terminate signal to {process_info['name']} (PID: {process_info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                self.logger.warning(f"Could not terminate {process_info['name']}: {e}")
        
        # Wait for processes to terminate gracefully
        if terminated_pids:
            self.logger.info(f"Waiting up to {timeout} seconds for processes to terminate...")
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                still_running = []
                for pid in terminated_pids:
                    try:
                        if psutil.pid_exists(pid):
                            still_running.append(pid)
                    except:
                        pass
                
                if not still_running:
                    self.logger.info("All EA processes terminated successfully")
                    return True
                
                time.sleep(1)
            
            # If some processes are still running, try force kill
            if still_running:
                self.logger.warning(f"Force killing {len(still_running)} remaining processes")
                for pid in still_running:
                    try:
                        process = psutil.Process(pid)
                        process.kill()
                        self.logger.info(f"Force killed process PID: {pid}")
                    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                        self.logger.error(f"Could not force kill process PID {pid}: {e}")
                
                # Final check
                time.sleep(2)
                final_check = self.find_ea_processes()
                if final_check:
                    self.logger.error(f"Failed to terminate {len(final_check)} EA processes")
                    return False
        
        self.logger.info("EA process termination completed")
        return True
    
    def wait_for_process_shutdown(self, timeout=30):
        """Wait for all EA processes to shut down completely"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            running_processes = self.find_ea_processes()
            if not running_processes:
                return True
            
            self.logger.info(f"Still waiting for {len(running_processes)} EA processes to shut down...")
            time.sleep(2)
        
        # Timeout reached
        remaining_processes = self.find_ea_processes()
        if remaining_processes:
            self.logger.warning(f"Timeout reached. {len(remaining_processes)} EA processes still running")
            return False
        
        return True
    
    def is_ea_running(self):
        """Check if any EA processes are currently running"""
        return len(self.find_ea_processes()) > 0
    
    def get_process_details(self, pid):
        """Get detailed information about a specific process"""
        try:
            process = psutil.Process(pid)
            return {
                'pid': pid,
                'name': process.name(),
                'exe': process.exe(),
                'cmdline': process.cmdline(),
                'status': process.status(),
                'create_time': process.create_time(),
                'memory_info': process.memory_info()._asdict(),
                'cpu_percent': process.cpu_percent()
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            self.logger.error(f"Could not get details for process PID {pid}: {e}")
            return None
    
    def kill_process_tree(self, pid):
        """Kill a process and all its children"""
        try:
            parent = psutil.Process(pid)
            children = parent.children(recursive=True)
            
            # Terminate children first
            for child in children:
                try:
                    child.terminate()
                    self.logger.info(f"Terminated child process: {child.name()} (PID: {child.pid})")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Terminate parent
            parent.terminate()
            self.logger.info(f"Terminated parent process: {parent.name()} (PID: {pid})")
            
            # Wait for termination
            gone, still_alive = psutil.wait_procs(children + [parent], timeout=10)
            
            # Force kill any remaining processes
            for process in still_alive:
                try:
                    process.kill()
                    self.logger.info(f"Force killed process: {process.name()} (PID: {process.pid})")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            return True
            
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            self.logger.error(f"Could not kill process tree for PID {pid}: {e}")
            return False