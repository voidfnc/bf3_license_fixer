"""
Icon Manager for BF3 License Fixer
Handles creation and management of application icons and graphics
"""

import tkinter as tk
from tkinter import PhotoImage
import base64
from io import BytesIO


class IconManager:
    """Manages icons and graphics for the application"""
    
    def __init__(self):
        self.icons = {}
        self.create_icons()
    
    def create_icons(self):
        """Create application icons from embedded data"""
        # Create simple geometric icons using tkinter
        self.icons['app'] = self.create_app_icon()
        self.icons['fix'] = self.create_fix_icon()
        self.icons['restore'] = self.create_restore_icon()
        self.icons['clear'] = self.create_clear_icon()
        self.icons['success'] = self.create_success_icon()
        self.icons['warning'] = self.create_warning_icon()
        self.icons['error'] = self.create_error_icon()
        self.icons['info'] = self.create_info_icon()
    
    def create_app_icon(self):
        """Create main application icon"""
        # Create a simple geometric app icon
        return self.create_geometric_icon(32, 32, '#007acc', 'app')
    
    def create_fix_icon(self):
        """Create fix/repair icon"""
        return self.create_geometric_icon(16, 16, '#4caf50', 'fix')
    
    def create_restore_icon(self):
        """Create restore icon"""
        return self.create_geometric_icon(16, 16, '#ff9800', 'restore')
    
    def create_clear_icon(self):
        """Create clear icon"""
        return self.create_geometric_icon(16, 16, '#f44336', 'clear')
    
    def create_success_icon(self):
        """Create success icon"""
        return self.create_geometric_icon(16, 16, '#4caf50', 'success')
    
    def create_warning_icon(self):
        """Create warning icon"""
        return self.create_geometric_icon(16, 16, '#ff9800', 'warning')
    
    def create_error_icon(self):
        """Create error icon"""
        return self.create_geometric_icon(16, 16, '#f44336', 'error')
    
    def create_info_icon(self):
        """Create info icon"""
        return self.create_geometric_icon(16, 16, '#2196f3', 'info')
    
    def create_geometric_icon(self, width, height, color, icon_type):
        """Create a geometric icon using Canvas"""
        # For now, return None as we'll create icons dynamically in the UI
        # This method is a placeholder for future icon implementation
        return None
    
    def get_icon(self, name):
        """Get an icon by name"""
        return self.icons.get(name)
    
    def create_status_indicator(self, parent, status='info', size=16):
        """Create a status indicator widget"""
        canvas = tk.Canvas(parent, width=size, height=size, 
                          bg='#1e1e1e', highlightthickness=0)
        
        colors = {
            'info': '#2196f3',
            'success': '#4caf50',
            'warning': '#ff9800',
            'error': '#f44336'
        }
        
        color = colors.get(status, '#2196f3')
        
        # Draw a simple circle indicator
        margin = 2
        canvas.create_oval(margin, margin, size-margin, size-margin, 
                          fill=color, outline="")
        
        return canvas
    
    def create_button_icon(self, parent, icon_type, size=16):
        """Create an icon for buttons"""
        canvas = tk.Canvas(parent, width=size, height=size, 
                          bg='transparent', highlightthickness=0)
        
        if icon_type == 'fix':
            # Draw a wrench-like icon
            self.draw_fix_icon(canvas, size)
        elif icon_type == 'restore':
            # Draw a circular arrow icon
            self.draw_restore_icon(canvas, size)
        elif icon_type == 'clear':
            # Draw an X icon
            self.draw_clear_icon(canvas, size)
        elif icon_type == 'settings':
            # Draw a gear icon
            self.draw_settings_icon(canvas, size)
        
        return canvas
    
    def draw_fix_icon(self, canvas, size):
        """Draw a fix/wrench icon"""
        color = '#ffffff'
        center = size // 2
        
        # Simple wrench representation
        canvas.create_rectangle(center-2, 2, center+2, size-2, 
                              fill=color, outline="")
        canvas.create_rectangle(2, center-2, size-2, center+2, 
                              fill=color, outline="")
    
    def draw_restore_icon(self, canvas, size):
        """Draw a restore/circular arrow icon"""
        color = '#ffffff'
        center = size // 2
        radius = size // 3
        
        # Draw circular arrow (simplified as arc)
        canvas.create_arc(center-radius, center-radius, 
                         center+radius, center+radius,
                         start=45, extent=270, width=2, 
                         outline=color, style='arc')
        
        # Arrow head
        canvas.create_polygon(center+radius-2, center-4,
                            center+radius+2, center,
                            center+radius-2, center+4,
                            fill=color, outline="")
    
    def draw_clear_icon(self, canvas, size):
        """Draw a clear/X icon"""
        color = '#ffffff'
        margin = 4
        
        # Draw X
        canvas.create_line(margin, margin, size-margin, size-margin, 
                          fill=color, width=2)
        canvas.create_line(size-margin, margin, margin, size-margin, 
                          fill=color, width=2)
    
    def draw_settings_icon(self, canvas, size):
        """Draw a settings/gear icon"""
        color = '#ffffff'
        center = size // 2
        
        # Simple gear representation
        canvas.create_oval(center-4, center-4, center+4, center+4, 
                          outline=color, width=2)
        canvas.create_oval(center-2, center-2, center+2, center+2, 
                          fill=color, outline="")


class ModernProgressBar:
    """Custom modern progress bar"""
    
    def __init__(self, parent, width=300, height=6):
        self.parent = parent
        self.width = width
        self.height = height
        self.progress = 0
        self.is_indeterminate = False
        self.animation_pos = 0
        
        self.canvas = tk.Canvas(parent, width=width, height=height,
                               bg='#1e1e1e', highlightthickness=0)
        
        # Colors
        self.bg_color = '#2d2d2d'
        self.fg_color = '#007acc'
        
        self.draw_progress()
    
    def pack(self, **kwargs):
        """Pack the canvas"""
        self.canvas.pack(**kwargs)
    
    def grid(self, **kwargs):
        """Grid the canvas"""
        self.canvas.grid(**kwargs)
    
    def draw_progress(self):
        """Draw the progress bar"""
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(0, 0, self.width, self.height,
                                   fill=self.bg_color, outline="")
        
        if self.is_indeterminate:
            # Animated indeterminate progress
            bar_width = 60
            x = (self.animation_pos * (self.width + bar_width)) // 100 - bar_width
            
            if x < self.width:
                # Create gradient effect with multiple rectangles
                for i in range(bar_width):
                    alpha = 1 - (i / bar_width)
                    if x + i >= 0 and x + i < self.width:
                        color = self.blend_colors(self.bg_color, self.fg_color, alpha)
                        self.canvas.create_line(x + i, 0, x + i, self.height,
                                              fill=color, width=1)
        else:
            # Determinate progress
            fill_width = (self.progress * self.width) // 100
            if fill_width > 0:
                self.canvas.create_rectangle(0, 0, fill_width, self.height,
                                           fill=self.fg_color, outline="")
    
    def set_progress(self, value):
        """Set progress value (0-100)"""
        self.progress = max(0, min(100, value))
        self.is_indeterminate = False
        self.draw_progress()
    
    def start_indeterminate(self):
        """Start indeterminate animation"""
        self.is_indeterminate = True
        self.animate_indeterminate()
    
    def stop_indeterminate(self):
        """Stop indeterminate animation"""
        self.is_indeterminate = False
        self.draw_progress()
    
    def animate_indeterminate(self):
        """Animate indeterminate progress"""
        if self.is_indeterminate:
            self.animation_pos = (self.animation_pos + 2) % 100
            self.draw_progress()
            self.parent.after(50, self.animate_indeterminate)
    
    def blend_colors(self, color1, color2, alpha):
        """Blend two hex colors"""
        # Simple color blending (placeholder)
        return color2 if alpha > 0.5 else color1


class ModernCard:
    """Modern card component"""
    
    def __init__(self, parent, title="", **kwargs):
        self.frame = tk.Frame(parent, bg='#2d2d2d', relief='solid', 
                             borderwidth=1, **kwargs)
        
        # Title if provided
        if title:
            title_label = tk.Label(self.frame, text=title, 
                                 bg='#2d2d2d', fg='#ffffff',
                                 font=('Segoe UI', 10, 'bold'),
                                 anchor='w')
            title_label.pack(fill='x', padx=15, pady=(15, 5))
        
        # Content frame
        self.content_frame = tk.Frame(self.frame, bg='#2d2d2d')
        self.content_frame.pack(fill='both', expand=True, padx=15, pady=15)
    
    def pack(self, **kwargs):
        """Pack the card"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """Grid the card"""
        self.frame.grid(**kwargs)


class LoadingSpinner:
    """Modern loading spinner"""
    
    def __init__(self, parent, size=32):
        self.parent = parent
        self.size = size
        self.angle = 0
        self.is_spinning = False
        
        self.canvas = tk.Canvas(parent, width=size, height=size,
                               bg='#1e1e1e', highlightthickness=0)
        
        self.color = '#007acc'
        self.draw_spinner()
    
    def pack(self, **kwargs):
        """Pack the canvas"""
        self.canvas.pack(**kwargs)
    
    def grid(self, **kwargs):
        """Grid the canvas"""
        self.canvas.grid(**kwargs)
    
    def draw_spinner(self):
        """Draw the loading spinner"""
        self.canvas.delete("all")
        
        center = self.size // 2
        radius = self.size // 3
        
        # Draw multiple arcs with varying opacity
        for i in range(8):
            start_angle = (self.angle + i * 45) % 360
            alpha = 1 - (i / 8)
            
            # Simple arc representation
            if alpha > 0.3:
                self.canvas.create_arc(center - radius, center - radius,
                                     center + radius, center + radius,
                                     start=start_angle, extent=30,
                                     outline=self.color, width=3,
                                     style='arc')
    
    def start(self):
        """Start spinning animation"""
        self.is_spinning = True
        self.spin()
    
    def stop(self):
        """Stop spinning animation"""
        self.is_spinning = False
    
    def spin(self):
        """Animate the spinner"""
        if self.is_spinning:
            self.angle = (self.angle + 15) % 360
            self.draw_spinner()
            self.parent.after(100, self.spin)
