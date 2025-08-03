"""
File Manager - Handles license file deletion and cache clearing operations
"""

import os
import shutil
import logging
from pathlib import Path
import glob


class FileManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        # Define target license files
        self.license_files = [
            '71067.dlf',  # BF3 license file
            '70619.dlf',  # Additional BF3 license file
            '70169.dlf'   # Another BF3 license file
        ]
        
        # Define paths
        self.license_path = Path(os.environ.get('PROGRAMDATA', 'C:\\ProgramData')) / 'Electronic Arts' / 'EA Services' / 'License'
        self.cache_path = Path(os.environ.get('PROGRAMDATA', 'C:\\ProgramData')) / 'Origin' / 'DownloadCache'
        
        # Alternative paths to check
        self.alternative_license_paths = [
            Path(os.environ.get('PROGRAMDATA', 'C:\\ProgramData')) / 'EA Core' / 'cache',
            Path(os.environ.get('PROGRAMDATA', 'C:\\ProgramData')) / 'Electronic Arts' / 'EA Desktop' / 'cache',
            Path(os.environ.get('PROGRAMDATA', 'C:\\ProgramData')) / 'Electronic Arts' / 'cache'
        ]
    
    def validate_paths(self):
        """Validate that the required paths exist"""
        results = {
            'license_path_exists': self.license_path.exists(),
            'cache_path_exists': self.cache_path.exists(),
            'alternative_paths': []
        }
        
        # Check alternative paths
        for alt_path in self.alternative_license_paths:
            if alt_path.exists():
                results['alternative_paths'].append(str(alt_path))
        
        self.logger.info(f"License path exists: {results['license_path_exists']} ({self.license_path})")
        self.logger.info(f"Cache path exists: {results['cache_path_exists']} ({self.cache_path})")
        
        if results['alternative_paths']:
            self.logger.info(f"Found alternative paths: {results['alternative_paths']}")
        
        return results
    
    def find_license_files(self):
        """Find all target license files in the system"""
        found_files = []
        
        # Check main license directory
        if self.license_path.exists():
            for license_file in self.license_files:
                file_path = self.license_path / license_file
                if file_path.exists():
                    found_files.append(str(file_path))
                    self.logger.info(f"Found license file: {file_path}")
        
        # Check alternative directories
        for alt_path in self.alternative_license_paths:
            if alt_path.exists():
                for license_file in self.license_files:
                    # Search recursively in alternative paths
                    pattern = str(alt_path / '**' / license_file)
                    matches = glob.glob(pattern, recursive=True)
                    for match in matches:
                        if match not in found_files:
                            found_files.append(match)
                            self.logger.info(f"Found license file in alternative location: {match}")
        
        return found_files
    
    def delete_license_files(self):
        """Delete all found license files"""
        found_files = self.find_license_files()
        deleted_files = []
        
        if not found_files:
            self.logger.info("No license files found to delete")
            return deleted_files
        
        for file_path in found_files:
            try:
                # Verify file still exists before deletion
                if os.path.exists(file_path):
                    # Check if file is read-only and remove attribute if needed
                    if os.path.isfile(file_path):
                        file_attrs = os.stat(file_path).st_mode
                        if not (file_attrs & 0o200):  # Check if write permission is missing
                            os.chmod(file_path, file_attrs | 0o200)  # Add write permission
                    
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    self.logger.info(f"Successfully deleted: {file_path}")
                else:
                    self.logger.warning(f"File no longer exists: {file_path}")
                    
            except PermissionError as e:
                self.logger.error(f"Permission denied deleting {file_path}: {e}")
            except FileNotFoundError as e:
                self.logger.warning(f"File not found during deletion {file_path}: {e}")
            except Exception as e:
                self.logger.error(f"Error deleting {file_path}: {e}")
        
        self.logger.info(f"Deleted {len(deleted_files)} out of {len(found_files)} license files")
        return deleted_files
    
    def clear_download_cache(self):
        """Clear the Origin download cache directory"""
        if not self.cache_path.exists():
            self.logger.info(f"Download cache directory does not exist: {self.cache_path}")
            return False
        
        try:
            # Get list of items in cache directory
            cache_items = list(self.cache_path.iterdir())
            
            if not cache_items:
                self.logger.info("Download cache directory is already empty")
                return True
            
            deleted_count = 0
            error_count = 0
            
            for item in cache_items:
                try:
                    if item.is_file():
                        # Remove read-only attribute if present
                        if not os.access(item, os.W_OK):
                            os.chmod(item, 0o777)
                        item.unlink()
                        deleted_count += 1
                        self.logger.debug(f"Deleted cache file: {item}")
                    elif item.is_dir():
                        shutil.rmtree(item, ignore_errors=False)
                        deleted_count += 1
                        self.logger.debug(f"Deleted cache directory: {item}")
                except PermissionError as e:
                    self.logger.error(f"Permission denied deleting cache item {item}: {e}")
                    error_count += 1
                except Exception as e:
                    self.logger.error(f"Error deleting cache item {item}: {e}")
                    error_count += 1
            
            self.logger.info(f"Cache cleanup completed: {deleted_count} items deleted, {error_count} errors")
            return error_count == 0
            
        except Exception as e:
            self.logger.error(f"Error clearing download cache: {e}")
            return False
    
    def get_file_info(self, file_path):
        """Get detailed information about a file"""
        try:
            path = Path(file_path)
            if not path.exists():
                return None
            
            stat = path.stat()
            return {
                'path': str(path),
                'size': stat.st_size,
                'modified': stat.st_mtime,
                'created': stat.st_ctime,
                'is_readonly': not (stat.st_mode & 0o200),
                'permissions': oct(stat.st_mode)[-3:]
            }
        except Exception as e:
            self.logger.error(f"Error getting file info for {file_path}: {e}")
            return None
    
    def safe_delete_file(self, file_path):
        """Safely delete a single file with proper error handling"""
        try:
            path = Path(file_path)
            
            if not path.exists():
                self.logger.warning(f"File does not exist: {file_path}")
                return False
            
            # Check if file is in use
            try:
                with open(path, 'r+b'):
                    pass
            except PermissionError:
                self.logger.error(f"File is in use and cannot be deleted: {file_path}")
                return False
            
            # Remove read-only attribute if present
            if not os.access(path, os.W_OK):
                os.chmod(path, 0o777)
            
            # Delete the file
            path.unlink()
            self.logger.info(f"Successfully deleted: {file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error deleting file {file_path}: {e}")
            return False
    
    def create_directory_if_not_exists(self, dir_path):
        """Create directory if it doesn't exist"""
        try:
            path = Path(dir_path)
            path.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Directory ensured: {dir_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error creating directory {dir_path}: {e}")
            return False
    
    def get_directory_size(self, dir_path):
        """Calculate total size of directory and its contents"""
        try:
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(dir_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(file_path)
                    except (OSError, FileNotFoundError):
                        pass
            return total_size
        except Exception as e:
            self.logger.error(f"Error calculating directory size for {dir_path}: {e}")
            return 0