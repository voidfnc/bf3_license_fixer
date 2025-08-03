"""
Modern Theme Module for BF3 License Fixer
Provides modern styling and theming capabilities
"""

import tkinter as tk
from tkinter import ttk
import sys


class ModernTheme:
    """Modern dark theme for the application"""
    
    # Color scheme - Modern dark theme
    COLORS = {
        'bg_primary': '#1e1e1e',        # Main background
        'bg_secondary': '#2d2d2d',      # Secondary background
        'bg_tertiary': '#3e3e3e',       # Tertiary background
        'bg_button': '#404040',         # Button background
        'bg_button_hover': '#4a4a4a',   # Button hover
        'bg_button_active': '#505050',  # Button active
        'bg_accent': '#007acc',         # Accent color (VS Code blue)
        'bg_accent_hover': '#1177dd',   # Accent hover
        'bg_success': '#4caf50',        # Success green
        'bg_warning': '#ff9800',        # Warning orange
        'bg_error': '#f44336',          # Error red
        'fg_primary': '#ffffff',        # Primary text
        'fg_secondary': '#cccccc',      # Secondary text
        'fg_disabled': '#888888',       # Disabled text
        'border': '#555555',            # Border color
        'border_focus': '#007acc',      # Focus border
    }
    
    # Fonts
    FONTS = {
        'default': ('Segoe UI', 9),
        'heading': ('Segoe UI', 12, 'bold'),
        'title': ('Segoe UI', 16, 'bold'),
        'button': ('Segoe UI', 9),
        'mono': ('Consolas', 9),
    }
    
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        self.setup_theme()
    
    def setup_theme(self):
        """Configure the modern theme"""
        # Set the theme
        self.style.theme_use('clam')
        
        # Configure root window
        self.root.configure(bg=self.COLORS['bg_primary'])
        
        # Configure styles
        self.configure_frame_styles()
        self.configure_label_styles()
        self.configure_button_styles()
        self.configure_entry_styles()
        self.configure_text_styles()
        self.configure_progressbar_styles()
        self.configure_scrollbar_styles()
    
    def configure_frame_styles(self):
        """Configure frame styles"""
        self.style.configure('Modern.TFrame',
                           background=self.COLORS['bg_primary'],
                           borderwidth=0)
        
        self.style.configure('Card.TFrame',
                           background=self.COLORS['bg_secondary'],
                           borderwidth=1,
                           relief='solid',
                           bordercolor=self.COLORS['border'])
        
        self.style.configure('Modern.TLabelFrame',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=1,
                           relief='solid',
                           bordercolor=self.COLORS['border'])
        
        self.style.configure('Modern.TLabelFrame.Label',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['fg_primary'],
                           font=self.FONTS['default'])
    
    def configure_label_styles(self):
        """Configure label styles"""
        self.style.configure('Modern.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['fg_primary'],
                           font=self.FONTS['default'])
        
        self.style.configure('Title.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['fg_primary'],
                           font=self.FONTS['title'])
        
        self.style.configure('Heading.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['fg_primary'],
                           font=self.FONTS['heading'])
        
        self.style.configure('Success.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['bg_success'],
                           font=self.FONTS['default'])
        
        self.style.configure('Warning.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['bg_warning'],
                           font=self.FONTS['default'])
        
        self.style.configure('Error.TLabel',
                           background=self.COLORS['bg_primary'],
                           foreground=self.COLORS['bg_error'],
                           font=self.FONTS['default'])
    
    def configure_button_styles(self):
        """Configure button styles"""
        # Primary button (accent)
        self.style.configure('Accent.TButton',
                           background=self.COLORS['bg_accent'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=0,
                           focuscolor='none',
                           font=self.FONTS['button'],
                           padding=(20, 10))
        
        self.style.map('Accent.TButton',
                     background=[('active', self.COLORS['bg_accent_hover']),
                               ('pressed', self.COLORS['bg_accent'])])
        
        # Secondary button
        self.style.configure('Secondary.TButton',
                           background=self.COLORS['bg_button'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=1,
                           relief='solid',
                           bordercolor=self.COLORS['border'],
                           focuscolor='none',
                           font=self.FONTS['button'],
                           padding=(15, 8))
        
        self.style.map('Secondary.TButton',
                     background=[('active', self.COLORS['bg_button_hover']),
                               ('pressed', self.COLORS['bg_button_active'])],
                     bordercolor=[('focus', self.COLORS['border_focus'])])
        
        # Success button
        self.style.configure('Success.TButton',
                           background=self.COLORS['bg_success'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=0,
                           focuscolor='none',
                           font=self.FONTS['button'],
                           padding=(15, 8))
        
        # Warning button
        self.style.configure('Warning.TButton',
                           background=self.COLORS['bg_warning'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=0,
                           focuscolor='none',
                           font=self.FONTS['button'],
                           padding=(15, 8))
    
    def configure_entry_styles(self):
        """Configure entry/input styles"""
        self.style.configure('Modern.TEntry',
                           fieldbackground=self.COLORS['bg_secondary'],
                           background=self.COLORS['bg_secondary'],
                           foreground=self.COLORS['fg_primary'],
                           borderwidth=1,
                           relief='solid',
                           bordercolor=self.COLORS['border'],
                           focuscolor=self.COLORS['border_focus'],
                           font=self.FONTS['default'],
                           padding=8)
        
        self.style.map('Modern.TEntry',
                     bordercolor=[('focus', self.COLORS['border_focus'])])
    
    def configure_text_styles(self):
        """Configure text widget styles (applied manually)"""
        # These will be applied to Text widgets manually since ttk doesn't style them
        pass
    
    def configure_progressbar_styles(self):
        """Configure progress bar styles"""
        self.style.configure('Modern.Horizontal.TProgressbar',
                           background=self.COLORS['bg_accent'],
                           troughcolor=self.COLORS['bg_secondary'],
                           borderwidth=0,
                           lightcolor=self.COLORS['bg_accent'],
                           darkcolor=self.COLORS['bg_accent'])
    
    def configure_scrollbar_styles(self):
        """Configure scrollbar styles"""
        self.style.configure('Modern.Vertical.TScrollbar',
                           background=self.COLORS['bg_secondary'],
                           troughcolor=self.COLORS['bg_primary'],
                           borderwidth=0,
                           arrowcolor=self.COLORS['fg_secondary'],
                           activebackground=self.COLORS['bg_button_hover'])
    
    def get_text_widget_config(self):
        """Get configuration for Text widgets"""
        return {
            'bg': self.COLORS['bg_secondary'],
            'fg': self.COLORS['fg_primary'],
            'insertbackground': self.COLORS['fg_primary'],
            'selectbackground': self.COLORS['bg_accent'],
            'selectforeground': self.COLORS['fg_primary'],
            'borderwidth': 1,
            'relief': 'solid',
            'highlightthickness': 1,
            'highlightcolor': self.COLORS['border_focus'],
            'highlightbackground': self.COLORS['border'],
            'font': self.FONTS['mono'],
            'wrap': tk.WORD,
            'padx': 10,
            'pady': 10
        }
    
    def get_listbox_config(self):
        """Get configuration for Listbox widgets"""
        return {
            'bg': self.COLORS['bg_secondary'],
            'fg': self.COLORS['fg_primary'],
            'selectbackground': self.COLORS['bg_accent'],
            'selectforeground': self.COLORS['fg_primary'],
            'borderwidth': 1,
            'relief': 'solid',
            'highlightthickness': 1,
            'highlightcolor': self.COLORS['border_focus'],
            'highlightbackground': self.COLORS['border'],
            'font': self.FONTS['default']
        }


class ModernTooltip:
    """Modern tooltip implementation"""
    
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind('<Enter>', self.on_enter)
        self.widget.bind('<Leave>', self.on_leave)
    
    def on_enter(self, event=None):
        """Show tooltip"""
        if self.tooltip:
            return
        
        x, y, _, _ = self.widget.bbox("insert") if hasattr(self.widget, 'bbox') else (0, 0, 0, 0)
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        # Modern tooltip styling
        label = tk.Label(self.tooltip, 
                        text=self.text,
                        background='#2d2d2d',
                        foreground='#ffffff',
                        font=('Segoe UI', 9),
                        relief='solid',
                        borderwidth=1,
                        padx=10,
                        pady=5)
        label.pack()
    
    def on_leave(self, event=None):
        """Hide tooltip"""
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class AnimatedButton(tk.Canvas):
    """Custom animated button with modern styling"""
    
    def __init__(self, parent, text="", command=None, style="primary", **kwargs):
        self.text = text
        self.command = command
        self.style_type = style
        
        # Default size
        width = kwargs.pop('width', 200)
        height = kwargs.pop('height', 40)
        
        super().__init__(parent, width=width, height=height, 
                        highlightthickness=0, **kwargs)
        
        # Colors based on style
        if style == "primary":
            self.bg_color = '#007acc'
            self.hover_color = '#1177dd'
            self.text_color = '#ffffff'
        elif style == "success":
            self.bg_color = '#4caf50'
            self.hover_color = '#5cbf60'
            self.text_color = '#ffffff'
        elif style == "warning":
            self.bg_color = '#ff9800'
            self.hover_color = '#ffab33'
            self.text_color = '#ffffff'
        elif style == "secondary":
            self.bg_color = '#404040'
            self.hover_color = '#4a4a4a'
            self.text_color = '#ffffff'
        
        self.current_color = self.bg_color
        self.configure(bg='#1e1e1e')
        
        # Draw initial button
        self.draw_button()
        
        # Bind events
        self.bind('<Button-1>', self.on_click)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
    
    def draw_button(self):
        """Draw the button"""
        self.delete("all")
        
        # Get canvas dimensions
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        
        # Draw rounded rectangle
        radius = 6
        self.create_rounded_rect(2, 2, width-2, height-2, radius, 
                               fill=self.current_color, outline="")
        
        # Draw text
        self.create_text(width//2, height//2, text=self.text, 
                        fill=self.text_color, font=('Segoe UI', 9, 'bold'))
    
    def create_rounded_rect(self, x1, y1, x2, y2, radius=10, **kwargs):
        """Create a rounded rectangle"""
        points = []
        for x, y in [(x1, y1 + radius), (x1, y1), (x1 + radius, y1),
                     (x2 - radius, y1), (x2, y1), (x2, y1 + radius),
                     (x2, y2 - radius), (x2, y2), (x2 - radius, y2),
                     (x1 + radius, y2), (x1, y2), (x1, y2 - radius)]:
            points.extend([x, y])
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def on_enter(self, event):
        """Handle mouse enter"""
        self.current_color = self.hover_color
        self.draw_button()
    
    def on_leave(self, event):
        """Handle mouse leave"""
        self.current_color = self.bg_color
        self.draw_button()
    
    def on_click(self, event):
        """Handle button click"""
        if self.command:
            self.command()
