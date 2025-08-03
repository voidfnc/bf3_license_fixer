#!/usr/bin/env python3
"""
BF3 License Fixer - Modern GUI Application
Direct launch to the modern dark theme interface
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
from pathlib import Path


def launch_modern():
    """Launch the modern GUI directly"""
    try:
        import main_modern
        main_modern.main()
    except ImportError as e:
        messagebox.showerror("Error", f"Could not load modern GUI: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch modern GUI: {e}")


if __name__ == "__main__":
    # Launch modern interface directly
    launch_modern()
