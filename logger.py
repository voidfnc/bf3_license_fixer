"""
Logger Configuration - Centralized logging setup for the BF3 License Fixer
"""

import logging
import logging.handlers
import os
from pathlib import Path
from datetime import datetime


class BF3Logger:
    def __init__(self, log_level=logging.INFO, log_to_file=True, log_to_console=True):
        self.log_level = log_level
        self.log_to_file = log_to_file
        self.log_to_console = log_to_console
        
        # Create logs directory
        self.log_dir = Path.home() / "Documents" / "BF3_License_Fixer_Logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
    
    def setup_logging(self):
        """Configure logging with file and console handlers"""
        # Create root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(self.log_level)
        
        # Clear any existing handlers
        root_logger.handlers.clear()
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Console handler
        if self.log_to_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.log_level)
            console_handler.setFormatter(formatter)
            root_logger.addHandler(console_handler)
        
        # File handler
        if self.log_to_file:
            log_filename = f"bf3_license_fixer_{datetime.now().strftime('%Y%m%d')}.log"
            log_file_path = self.log_dir / log_filename
            
            # Use rotating file handler to prevent huge log files
            file_handler = logging.handlers.RotatingFileHandler(
                log_file_path,
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5
            )
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)
        
        # Log the initialization
        logger = logging.getLogger(__name__)
        logger.info("BF3 License Fixer logging initialized")
        logger.info(f"Log level: {logging.getLevelName(self.log_level)}")
        if self.log_to_file:
            logger.info(f"Log directory: {self.log_dir}")
    
    def get_logger(self, name):
        """Get a logger instance for a specific module"""
        return logging.getLogger(name)
    
    def set_log_level(self, level):
        """Change the logging level"""
        self.log_level = level
        root_logger = logging.getLogger()
        root_logger.setLevel(level)
        
        # Update all handlers
        for handler in root_logger.handlers:
            handler.setLevel(level)
        
        logger = logging.getLogger(__name__)
        logger.info(f"Log level changed to: {logging.getLevelName(level)}")
    
    def cleanup_old_logs(self, days_to_keep=30):
        """Remove log files older than specified days"""
        try:
            cutoff_time = datetime.now().timestamp() - (days_to_keep * 24 * 60 * 60)
            deleted_count = 0
            
            for log_file in self.log_dir.glob("*.log*"):
                if log_file.stat().st_mtime < cutoff_time:
                    try:
                        log_file.unlink()
                        deleted_count += 1
                    except Exception as e:
                        logger = logging.getLogger(__name__)
                        logger.warning(f"Could not delete old log file {log_file}: {e}")
            
            if deleted_count > 0:
                logger = logging.getLogger(__name__)
                logger.info(f"Cleaned up {deleted_count} old log files")
                
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error during log cleanup: {e}")
    
    def get_log_files(self):
        """Get list of all log files"""
        try:
            log_files = []
            for log_file in self.log_dir.glob("*.log*"):
                log_files.append({
                    'path': str(log_file),
                    'name': log_file.name,
                    'size': log_file.stat().st_size,
                    'modified': datetime.fromtimestamp(log_file.stat().st_mtime)
                })
            
            # Sort by modification time (newest first)
            log_files.sort(key=lambda x: x['modified'], reverse=True)
            return log_files
            
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error getting log files: {e}")
            return []
    
    def get_recent_logs(self, lines=100):
        """Get recent log entries"""
        log_files = self.get_log_files()
        
        if not log_files:
            return []
        
        # Read from the most recent log file
        recent_log_file = log_files[0]['path']
        
        try:
            with open(recent_log_file, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                return all_lines[-lines:] if len(all_lines) > lines else all_lines
                
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Error reading recent logs: {e}")
            return []


# Global logger instance
_bf3_logger = None


def initialize_logging(log_level=logging.INFO, log_to_file=True, log_to_console=True):
    """Initialize the global logger"""
    global _bf3_logger
    _bf3_logger = BF3Logger(log_level, log_to_file, log_to_console)
    return _bf3_logger


def get_logger(name=None):
    """Get a logger instance"""
    global _bf3_logger
    
    if _bf3_logger is None:
        _bf3_logger = initialize_logging()
    
    if name is None:
        name = __name__
    
    return _bf3_logger.get_logger(name)


def set_log_level(level):
    """Set the global log level"""
    global _bf3_logger
    
    if _bf3_logger is None:
        _bf3_logger = initialize_logging()
    
    _bf3_logger.set_log_level(level)


def cleanup_old_logs(days_to_keep=30):
    """Clean up old log files"""
    global _bf3_logger
    
    if _bf3_logger is None:
        _bf3_logger = initialize_logging()
    
    _bf3_logger.cleanup_old_logs(days_to_keep)


def get_recent_logs(lines=100):
    """Get recent log entries"""
    global _bf3_logger
    
    if _bf3_logger is None:
        _bf3_logger = initialize_logging()
    
    return _bf3_logger.get_recent_logs(lines)