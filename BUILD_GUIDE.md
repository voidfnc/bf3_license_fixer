# BF3 License Fixer - Build Guide

## Overview
This project now includes professional build configuration with:
- **Custom Application Icon** (`app_icon.ico`)
- **Professional Metadata** to avoid antivirus false positives
- **Author Information** (@voidfnc)
- **GitHub URL** and project details
- **Version Information** and copyright details

## Build Scripts Available

### 1. `build.bat` (Main Build Script)
- **Complete professional build** with all features
- **Includes icon and metadata** automatically
- **Auto-generates version info** with @voidfnc attribution
- **Smart Python detection** (tries `py` then `python`)
- **Professional executable output**

### 2. `build_debug.bat` (Debug Only)
- **Debug version** with detailed output
- **For troubleshooting** build issues

## Quick Start

1. **Install Dependencies:**
   ```bash
   setup.bat
   ```

2. **Build Executable:**
   ```bash
   build.bat
   ```

## Files Created

### `version_info.txt`
Contains Windows executable metadata:
- **Company Name:** Voidfnc (@voidfnc)
- **Product Name:** BF3 License Fixer
- **Description:** Battlefield 3 License Activation Tool
- **Copyright:** MIT License
- **GitHub URL:** https://github.com/voidfnc/bf3_license_fixer
- **Version:** 1.2.0

### `BF3_License_Fixer.spec`
PyInstaller specification file with:
- **Icon integration:** `app_icon.ico`
- **Version file:** `version_info.txt`
- **Theme bundling:** `themes` directory
- **Hidden imports:** All required modules
- **Windowed mode:** No console window

## Anti-Virus Protection

The executable now includes:
- ✅ **Digital signature metadata**
- ✅ **Company information**
- ✅ **Product description**
- ✅ **Copyright details**
- ✅ **Version information**
- ✅ **GitHub source URL**

This metadata helps antivirus software recognize the executable as legitimate software.

## Output

The final executable will be located at:
```
dist/BF3_License_Fixer.exe
```

Features included:
- **Professional icon**
- **No console window**
- **All themes bundled**
- **Complete dependency inclusion**
- **Windows metadata**
- **Antivirus-friendly attributes**

## Distribution

The executable is now ready for distribution and should trigger fewer false positives from antivirus software due to the comprehensive metadata included.
