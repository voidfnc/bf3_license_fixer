# 🎮 BF3 License Fixer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Build](https://img.shields.io/badge/Build-Passing-green.svg)]()

> **Modern Windows application to fix Battlefield 3 "Could not activate license" errors in EA App and Origin**

![BF3 License Fixer](assets/screenshot.png)

## 🚀 **Quick Start**

### 📥 **Download Ready-to-Use Executable**
1. Go to [**Releases**](../../releases)
2. Download `BF3_License_Fixer.exe`
3. Run the executable - **No installation required!**

### 🛠️ **Build from Source**
```bash
# Clone the repository
git clone https://github.com/voidfnc/bf3_license_fixer.git
cd bf3_license_fixer

# Install dependencies
.\setup.bat

# Build executable
.\build.bat
```

## ❓ **What This Fixes**

### 🎯 **The Problem**
Battlefield 3 players often encounter this frustrating error:
- **"Could not activate license"** in EA App
- **"License not found"** in Origin
- Game appears in library but **won't launch**
- **Infinite loading** or **activation loops**

### ✅ **The Solution**
This tool **automatically fixes** the license activation by:
- 🔍 **Detecting** EA App and Origin processes
- 📁 **Locating** game installation directories
- 🗂️ **Managing** license and cache files
- 🔧 **Repairing** corrupted activation data
- 🔄 **Restarting** necessary services

## 🎨 **Features**

### 🖥️ **Modern Interface**
- **Dark theme** inspired by VS Code
- **Intuitive GUI** with clear status indicators  
- **Real-time progress** updates
- **Detailed logging** with timestamps

### 🛡️ **Safe & Reliable**
- ✅ **Automatic backups** before any changes
- ✅ **Process detection** to avoid conflicts
- ✅ **Rollback functionality** if needed
- ✅ **Non-destructive** operations

### ⚡ **Smart Automation**
- 🎯 **Auto-detects** EA App and Origin installations
- 🔄 **Handles multiple** installation paths
- 📊 **Progress tracking** with detailed status
- 🗝️ **One-click solution** for most cases

## 🔧 **System Requirements**

- **Windows 10/11** (64-bit)
- **Battlefield 3** installed via EA App or Origin
- **Administrator privileges** (for file operations)

## 📖 **Usage Guide**

### 🎮 **For Gamers (Easy)**
1. **Download** the latest `BF3_License_Fixer.exe` from [Releases](../../releases)
2. **Run as Administrator** (right-click → "Run as administrator")
3. **Click "Start Fix"** and wait for completion
4. **Launch Battlefield 3** - the error should be resolved!

### 👨‍💻 **For Developers**
```bash
# Clone and setup
git clone https://github.com/voidfnc/bf3-license-fixer.git
cd bf3-license-fixer
.\setup.bat

# Run from source
python main_modern.py

# Build executable
.\build.bat
```

## 🗂️ **Project Structure**
```
bf3-license-fixer/
├── 🎯 main_modern.py          # Main application entry point
├── 🎨 themes/                 # Modern dark theme files
├── 🔧 backup_manager.py       # Backup and restore functionality
├── 📁 file_manager.py         # File operations and utilities
├── ⚙️ process_manager.py      # Process detection and management
├── 📝 logger.py               # Logging system
├── 🏗️ build.bat              # Main build script
├── 📦 setup.bat               # Dependency installer
├── ⚙️ BF3_License_Fixer.spec  # PyInstaller configuration
├── 🎨 app_icon.ico            # Application icon
└── 📚 docs/                   # Documentation files
```

## 🛠️ **Build System**

### 🚀 **Professional Build**
The project includes a **professional build system** that creates executables with:
- 🎨 **Custom application icon**
- 📋 **Professional metadata** (author, version, copyright)
- 🛡️ **Anti-virus friendly** signatures
- 🏷️ **Digital signature** information

### 📦 **Build Commands**
```bash
.\setup.bat       # Install Python dependencies
.\build.bat       # Build professional executable
.\build_debug.bat # Build debug version
```

**Output**: `dist/BF3_License_Fixer.exe` (~21MB standalone executable)

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### 🐛 **Found a Bug?**
- Check [existing issues](../../issues)
- Create a [new issue](../../issues/new) with details
- Include your **Windows version** and **EA App/Origin version**

### 💡 **Feature Request?**
- Open a [feature request](../../issues/new)
- Describe the **use case** and **expected behavior**

## 📝 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 📞 **Support**

- 🐛 **Issues**: [GitHub Issues](../../issues)
- 💬 **Discussions**: [GitHub Discussions](../../discussions)  
- 📧 **Contact**: [@voidfnc](https://github.com/voidfnc)

## 🙏 **Acknowledgments**

- **EA/DICE** for Battlefield 3
- **Python** community for excellent libraries
- **Contributors** who help improve this tool
- **Battlefield 3** community for testing and feedback

## ⚠️ **Disclaimer**

This tool is **not affiliated** with EA, DICE, or Battlefield. It's a **community solution** for a common technical issue. Use at your own discretion.

---

**Made with ❤️ by [@voidfnc](https://github.com/voidfnc) for the Battlefield 3 community**
