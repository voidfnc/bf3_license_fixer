#!/usr/bin/env python3
"""
BF3 License Fix Tool - Modern GUI Application
Fixes "Could not activate license" error in EA App/Origin for Battlefield 3
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import sys
import os
from pathlib import Path

# Import our custom modules
from process_manager import ProcessManager
from file_manager import FileManager
from backup_manager import BackupManager
from logger import initialize_logging, get_logger

# Import modern theme components
from themes.modern_theme import ModernTheme, ModernTooltip, AnimatedButton
from themes.icons import IconManager, ModernProgressBar, ModernCard, LoadingSpinner


class ModernBF3LicenseFixerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BF3 License Fixer v2.0")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        self.root.minsize(600, 500)
        
        # Initialize theme and icons
        self.theme = ModernTheme(root)
        self.icon_manager = IconManager()
        
        # Initialize managers
        self.process_manager = ProcessManager()
        self.file_manager = FileManager()
        self.backup_manager = BackupManager()
        
        # Initialize logging
        try:
            initialize_logging()
            self.logger = get_logger(__name__)
        except:
            # Fallback if logging fails
            import logging
            self.logger = logging.getLogger(__name__)
        
        # Setup modern GUI
        self.setup_modern_gui()
        
        # Check admin privileges on startup
        self.check_admin_privileges()
    
    def setup_modern_gui(self):
        """Create the modern GUI interface"""
        # Main container with padding
        main_container = ttk.Frame(self.root, style='Modern.TFrame', padding="20")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(2, weight=1)
        
        # Header section
        self.create_header(main_container)
        
        # Main content area
        self.create_main_content(main_container)
        
        # Footer section
        self.create_footer(main_container)
        
        # Initial setup
        self.log_message("BF3 License Fixer v2.0 initialized successfully", "success")
        self.log_message("Modern GUI theme loaded", "info")
        self.log_message("Click 'Start License Fix' to begin the repair process", "info")
    
    def create_header(self, parent):
        """Create the modern header section"""
        header_frame = ttk.Frame(parent, style='Modern.TFrame')
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        header_frame.columnconfigure(1, weight=1)
        
        # App icon placeholder (using colored rectangle for now)
        icon_canvas = tk.Canvas(header_frame, width=48, height=48, 
                               bg='#1e1e1e', highlightthickness=0)
        icon_canvas.grid(row=0, column=0, rowspan=2, padx=(0, 15))
        icon_canvas.create_oval(4, 4, 44, 44, fill='#007acc', outline='')
        icon_canvas.create_text(24, 24, text='BF3', fill='white', 
                               font=('Segoe UI', 12, 'bold'))
        
        # Title and subtitle
        title_label = ttk.Label(header_frame, text="BF3 License Fixer", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=1, sticky=(tk.W), pady=(0, 2))
        
        subtitle_label = ttk.Label(header_frame, 
                                  text="Fix 'Could not activate license' errors in Battlefield 3",
                                  style='Modern.TLabel')
        subtitle_label.grid(row=1, column=1, sticky=(tk.W))
        
        # Status indicator
        self.status_indicator = self.icon_manager.create_status_indicator(
            header_frame, 'info', 16)
        self.status_indicator.grid(row=0, column=2, padx=(10, 0))
    
    def create_main_content(self, parent):
        """Create the main content area"""
        content_frame = ttk.Frame(parent, style='Modern.TFrame')
        content_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(1, weight=1)
        
        # Action buttons section
        self.create_action_buttons(content_frame)
        
        # Log display section
        self.create_log_display(content_frame)
        
        # Progress section
        self.create_progress_section(content_frame)
    
    def create_action_buttons(self, parent):
        """Create modern action buttons"""
        button_frame = ttk.Frame(parent, style='Modern.TFrame')
        button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Create cards for different actions
        # Primary action card
        primary_card = ModernCard(button_frame, title="Quick Fix")
        primary_card.pack(fill='x', pady=(0, 10))
        
        primary_desc = tk.Label(primary_card.content_frame, 
                               text="Automatically fix license issues with one click",
                               bg='#2d2d2d', fg='#cccccc', 
                               font=('Segoe UI', 9), anchor='w')
        primary_desc.pack(fill='x', pady=(0, 10))
        
        self.fix_button = AnimatedButton(primary_card.content_frame, 
                                        text="🔧 Start License Fix",
                                        command=self.start_fix_process,
                                        style="primary", width=200, height=40)
        self.fix_button.pack(pady=5)
        
        # Secondary actions card
        secondary_card = ModernCard(button_frame, title="Additional Options")
        secondary_card.pack(fill='x', pady=(0, 10))
        
        secondary_frame = tk.Frame(secondary_card.content_frame, bg='#2d2d2d')
        secondary_frame.pack(fill='x')
        
        self.restore_button = AnimatedButton(secondary_frame,
                                           text="🔄 Restore Backup",
                                           command=self.restore_backup,
                                           style="secondary", width=140, height=35)
        self.restore_button.pack(side='left', padx=(0, 10))
        
        clear_button = AnimatedButton(secondary_frame,
                                     text="🗑️ Clear Log",
                                     command=self.clear_log,
                                     style="secondary", width=120, height=35)
        clear_button.pack(side='left')
        
        # Add tooltips
        ModernTooltip(self.fix_button, "Start the automated license fix process")
        ModernTooltip(self.restore_button, "Restore files from the most recent backup")
        ModernTooltip(clear_button, "Clear the operation log display")
    
    def create_log_display(self, parent):
        """Create modern log display"""
        log_card = ModernCard(parent, title="Operation Log")
        log_card.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create text widget with modern styling
        text_config = self.theme.get_text_widget_config()
        self.log_text = tk.Text(log_card.content_frame, height=15, **text_config)
        
        # Modern scrollbar
        scrollbar = ttk.Scrollbar(log_card.content_frame, style='Modern.Vertical.TScrollbar')
        
        # Pack text and scrollbar
        self.log_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Configure scrollbar
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
        
        # Configure text tags for colored output
        self.log_text.tag_configure("error", foreground="#f44336")
        self.log_text.tag_configure("warning", foreground="#ff9800")
        self.log_text.tag_configure("success", foreground="#4caf50")
        self.log_text.tag_configure("info", foreground="#2196f3")
        self.log_text.tag_configure("timestamp", foreground="#888888")
    
    def create_progress_section(self, parent):
        """Create modern progress section"""
        progress_frame = ttk.Frame(parent, style='Modern.TFrame')
        progress_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        progress_frame.columnconfigure(1, weight=1)
        
        # Loading spinner (hidden by default)
        self.spinner = LoadingSpinner(progress_frame, size=24)
        self.spinner.grid(row=0, column=0, padx=(0, 10))
        self.spinner.canvas.grid_remove()  # Hide initially
        
        # Modern progress bar
        self.progress_bar = ModernProgressBar(progress_frame, width=400, height=8)
        self.progress_bar.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(progress_frame, text="Ready to fix license issue",
                                     style='Success.TLabel')
        self.status_label.grid(row=0, column=2)
    
    def create_footer(self, parent):
        """Create modern footer"""
        footer_frame = ttk.Frame(parent, style='Modern.TFrame')
        footer_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        footer_frame.columnconfigure(0, weight=1)
        
        # Version and admin status
        info_text = "v2.0 • "
        try:
            import ctypes
            if ctypes.windll.shell32.IsUserAnAdmin():
                info_text += "Administrator privileges ✓"
            else:
                info_text += "Limited privileges ⚠️"
        except:
            info_text += "Unknown privileges"
        
        footer_label = ttk.Label(footer_frame, text=info_text, 
                                style='Modern.TLabel')
        footer_label.grid(row=0, column=0)
    
    def check_admin_privileges(self):
        """Check if running with administrator privileges"""
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                self.log_message("⚠️ Not running as administrator", "warning")
                self.log_message("Some operations may fail without admin privileges", "warning")
                self.update_status("Warning: Not running as administrator", "warning")
                # Update status indicator
                self.status_indicator.destroy()
                self.status_indicator = self.icon_manager.create_status_indicator(
                    self.status_indicator.master, 'warning', 16)
                self.status_indicator.grid(row=0, column=2, padx=(10, 0))
            else:
                self.log_message("✓ Running with administrator privileges", "success")
        except Exception as e:
            self.log_message(f"Could not check admin privileges: {e}", "error")
    
    def log_message(self, message, level="info"):
        """Add a message to the modern log display"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Icon mapping
        icons = {
            "error": "❌",
            "warning": "⚠️",
            "success": "✅",
            "info": "ℹ️"
        }
        
        icon = icons.get(level, "ℹ️")
        
        # Insert timestamp
        self.log_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        # Insert icon and message
        self.log_text.insert(tk.END, f"{icon} {message}\n", level)
        
        # Auto-scroll to bottom
        self.log_text.see(tk.END)
        
        # Log to file if logger is available
        try:
            if level == "error":
                self.logger.error(message)
            elif level == "warning":
                self.logger.warning(message)
            else:
                self.logger.info(message)
        except:
            pass
        
        # Update GUI
        self.root.update_idletasks()
    
    def clear_log(self):
        """Clear the log display"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("Log cleared", "info")
    
    def update_status(self, message, level="info"):
        """Update the status label with modern styling"""
        style_map = {
            "info": "Modern.TLabel",
            "success": "Success.TLabel",
            "warning": "Warning.TLabel",
            "error": "Error.TLabel"
        }
        
        style = style_map.get(level, "Modern.TLabel")
        self.status_label.config(text=message, style=style)
        self.root.update_idletasks()
    
    def start_fix_process(self):
        """Start the license fix process with modern UI updates"""
        # Disable buttons and show progress
        self.fix_button.configure(state="disabled")
        self.restore_button.configure(state="disabled")
        
        # Show spinner and start progress animation
        self.spinner.canvas.grid()
        self.spinner.start()
        self.progress_bar.start_indeterminate()
        
        # Update status
        self.update_status("Processing...", "info")
        
        # Run fix in separate thread
        fix_thread = threading.Thread(target=self.fix_license_issue)
        fix_thread.daemon = True
        fix_thread.start()
    
    def fix_license_issue(self):
        """Main fix process with enhanced logging"""
        try:
            self.update_status("Starting license fix process...", "info")
            self.log_message("=== Starting BF3 License Fix Process ===", "info")
            
            # Step 1: Check for running EA processes
            self.log_message("🔍 Step 1: Checking for running EA App/Origin processes...", "info")
            running_processes = self.process_manager.find_ea_processes()
            
            if running_processes:
                self.log_message(f"Found {len(running_processes)} EA processes running", "warning")
                for process in running_processes:
                    self.log_message(f"  • {process['name']} (PID: {process['pid']})", "info")
                
                # Terminate processes
                self.log_message("🔄 Terminating EA processes...", "info")
                if self.process_manager.terminate_ea_processes():
                    self.log_message("✅ Successfully terminated EA processes", "success")
                else:
                    self.log_message("⚠️ Failed to terminate some EA processes", "warning")
            else:
                self.log_message("✅ No EA processes found running", "success")
            
            # Step 2: Create backup
            self.log_message("💾 Step 2: Creating backup of license files...", "info")
            license_files = self.file_manager.find_license_files()
            if license_files:
                backup_path = self.backup_manager.create_backup(license_files)
                if backup_path:
                    self.log_message(f"✅ Backup created successfully: {backup_path}", "success")
                else:
                    self.log_message("⚠️ Failed to create backup", "warning")
            else:
                self.log_message("ℹ️ No license files found to backup", "warning")
                backup_path = None
            
            # Step 3: Delete license files
            self.log_message("🗑️ Step 3: Deleting corrupted license files...", "info")
            deleted_files = self.file_manager.delete_license_files()
            if deleted_files:
                self.log_message(f"✅ Successfully deleted {len(deleted_files)} license files:", "success")
                for file in deleted_files:
                    self.log_message(f"  • {file}", "info")
            else:
                self.log_message("ℹ️ No license files found to delete", "info")
            
            # Step 4: Clear download cache
            self.log_message("🧹 Step 4: Clearing Origin download cache...", "info")
            cache_cleared = self.file_manager.clear_download_cache()
            if cache_cleared:
                self.log_message("✅ Download cache cleared successfully", "success")
            else:
                self.log_message("ℹ️ Download cache not found or already empty", "info")
            
            # Step 5: Success message and instructions
            self.log_message("🎉 === License Fix Process Completed Successfully ===", "success")
            self.log_message("📋 Next steps:", "info")
            self.log_message("  1. Restart EA App or Origin", "info")
            self.log_message("  2. Log in to your EA account", "info")
            self.log_message("  3. Try launching Battlefield 3", "info")
            
            self.update_status("License fix completed successfully! 🎉", "success")
            
            # Show success dialog
            self.root.after(0, self.show_modern_success_dialog)
            
        except Exception as e:
            error_msg = f"An error occurred during the fix process: {str(e)}"
            self.log_message(f"❌ {error_msg}", "error")
            self.update_status("Fix process failed ❌", "error")
            
            # Show error dialog
            self.root.after(0, lambda: self.show_modern_error_dialog(error_msg))
        
        finally:
            # Re-enable buttons and stop progress
            self.root.after(0, self.finish_fix_process)
    
    def finish_fix_process(self):
        """Clean up after fix process with modern UI updates"""
        # Stop animations
        self.spinner.stop()
        self.spinner.canvas.grid_remove()
        self.progress_bar.stop_indeterminate()
        
        # Re-enable buttons
        self.fix_button.configure(state="normal")
        self.restore_button.configure(state="normal")
    
    def show_modern_success_dialog(self):
        """Show modern success dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Fix Completed Successfully")
        dialog.geometry("500x400")
        dialog.configure(bg='#1e1e1e')
        dialog.resizable(False, False)
        
        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Main frame
        main_frame = tk.Frame(dialog, bg='#1e1e1e', padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Success icon and title
        title_frame = tk.Frame(main_frame, bg='#1e1e1e')
        title_frame.pack(fill='x', pady=(0, 20))
        
        success_icon = tk.Label(title_frame, text="🎉", bg='#1e1e1e', 
                               font=('Segoe UI', 24))
        success_icon.pack()
        
        title_label = tk.Label(title_frame, text="License Fix Completed Successfully!",
                              bg='#1e1e1e', fg='#4caf50',
                              font=('Segoe UI', 14, 'bold'))
        title_label.pack(pady=(10, 0))
        
        # Instructions
        instructions = [
            "Your Battlefield 3 license has been fixed. Follow these steps:",
            "",
            "1. 🔄 Restart EA App or Origin",
            "2. 👤 Log in to your EA account",
            "3. 🎮 Try launching Battlefield 3",
            "",
            "If the issue persists, you can restore the backup using",
            "the 'Restore Backup' button in the main window."
        ]
        
        for instruction in instructions:
            label = tk.Label(main_frame, text=instruction, bg='#1e1e1e', 
                           fg='#ffffff', font=('Segoe UI', 10),
                           anchor='w', justify='left')
            label.pack(fill='x', pady=2)
        
        # Close button
        close_button = AnimatedButton(main_frame, text="Close",
                                     command=dialog.destroy,
                                     style="primary", width=100, height=35)
        close_button.pack(pady=(20, 0))
    
    def show_modern_error_dialog(self, error_msg):
        """Show modern error dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Error Occurred")
        dialog.geometry("450x300")
        dialog.configure(bg='#1e1e1e')
        dialog.resizable(False, False)
        
        # Center the dialog
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Main frame
        main_frame = tk.Frame(dialog, bg='#1e1e1e', padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Error icon and title
        title_frame = tk.Frame(main_frame, bg='#1e1e1e')
        title_frame.pack(fill='x', pady=(0, 20))
        
        error_icon = tk.Label(title_frame, text="❌", bg='#1e1e1e', 
                             font=('Segoe UI', 24))
        error_icon.pack()
        
        title_label = tk.Label(title_frame, text="An Error Occurred",
                              bg='#1e1e1e', fg='#f44336',
                              font=('Segoe UI', 14, 'bold'))
        title_label.pack(pady=(10, 0))
        
        # Error message
        msg_label = tk.Label(main_frame, text=error_msg, bg='#1e1e1e', 
                           fg='#ffffff', font=('Segoe UI', 10),
                           wraplength=390, justify='left')
        msg_label.pack(fill='x', pady=(0, 20))
        
        # Close button
        close_button = AnimatedButton(main_frame, text="Close",
                                     command=dialog.destroy,
                                     style="secondary", width=100, height=35)
        close_button.pack()
    
    def restore_backup(self):
        """Restore the most recent backup with modern UI"""
        try:
            self.log_message("🔄 Starting backup restore process...", "info")
            
            restored_files = self.backup_manager.restore_latest_backup()
            if restored_files:
                self.log_message(f"✅ Successfully restored {len(restored_files)} files:", "success")
                for file in restored_files:
                    self.log_message(f"  • {file}", "info")
                
                self.update_status("Backup restored successfully ✅", "success")
                
                # Show modern success message
                self.show_restore_success_dialog(len(restored_files))
            else:
                self.log_message("⚠️ No backup files found to restore", "warning")
                self.show_no_backup_dialog()
                
        except Exception as e:
            error_msg = f"Failed to restore backup: {str(e)}"
            self.log_message(f"❌ {error_msg}", "error")
            self.update_status("Backup restore failed ❌", "error")
            self.show_modern_error_dialog(error_msg)
    
    def show_restore_success_dialog(self, file_count):
        """Show restore success dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Restore Completed")
        dialog.geometry("400x250")
        dialog.configure(bg='#1e1e1e')
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        main_frame = tk.Frame(dialog, bg='#1e1e1e', padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Success content
        icon_label = tk.Label(main_frame, text="✅", bg='#1e1e1e', 
                             font=('Segoe UI', 24))
        icon_label.pack(pady=(0, 10))
        
        title_label = tk.Label(main_frame, text="Restore Completed",
                              bg='#1e1e1e', fg='#4caf50',
                              font=('Segoe UI', 14, 'bold'))
        title_label.pack(pady=(0, 10))
        
        msg_label = tk.Label(main_frame, 
                           text=f"Successfully restored {file_count} files from backup.",
                           bg='#1e1e1e', fg='#ffffff', font=('Segoe UI', 10))
        msg_label.pack(pady=(0, 20))
        
        close_button = AnimatedButton(main_frame, text="Close",
                                     command=dialog.destroy,
                                     style="primary", width=100, height=35)
        close_button.pack()
    
    def show_no_backup_dialog(self):
        """Show no backup available dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("No Backup Available")
        dialog.geometry("400x250")
        dialog.configure(bg='#1e1e1e')
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        main_frame = tk.Frame(dialog, bg='#1e1e1e', padx=30, pady=30)
        main_frame.pack(fill='both', expand=True)
        
        # Warning content
        icon_label = tk.Label(main_frame, text="⚠️", bg='#1e1e1e', 
                             font=('Segoe UI', 24))
        icon_label.pack(pady=(0, 10))
        
        title_label = tk.Label(main_frame, text="No Backup Available",
                              bg='#1e1e1e', fg='#ff9800',
                              font=('Segoe UI', 14, 'bold'))
        title_label.pack(pady=(0, 10))
        
        msg_label = tk.Label(main_frame, 
                           text="No backup files were found to restore.",
                           bg='#1e1e1e', fg='#ffffff', font=('Segoe UI', 10))
        msg_label.pack(pady=(0, 20))
        
        close_button = AnimatedButton(main_frame, text="Close",
                                     command=dialog.destroy,
                                     style="secondary", width=100, height=35)
        close_button.pack()


def main():
    """Main application entry point"""
    # Create the main window
    root = tk.Tk()
    
    # Set application icon (if available)
    try:
        if os.path.exists("assets/icon.ico"):
            root.iconbitmap("assets/icon.ico")
    except:
        pass  # Icon not critical
    
    # Create and run the modern application
    app = ModernBF3LicenseFixerGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
