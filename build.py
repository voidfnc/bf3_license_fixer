#!/usr/bin/env python3
"""
Build script for BF3 License Fixer
Creates a standalone executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_requirements():
    """Check if required packages are installed"""
    try:
        import PyInstaller
        print(f"✓ PyInstaller found: {PyInstaller.__version__}")
    except ImportError:
        print("✗ PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    try:
        import psutil
        print(f"✓ psutil found: {psutil.__version__}")
    except ImportError:
        print("✗ psutil not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])


def create_spec_file():
    """Create PyInstaller spec file for customized build"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main_modern.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('themes', 'themes'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'tkinter.scrolledtext',
        'psutil',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BF3_License_Fixer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='app_icon.ico',
    version='version_info.txt',
)
'''
    
    with open('BF3_License_Fixer.spec', 'w') as f:
        f.write(spec_content)
    
    print("✓ Spec file created: BF3_License_Fixer.spec")
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Filter out None values from datas
a.datas = [item for item in a.datas if item is not None]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BF3_License_Fixer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico' if os.path.exists('assets/icon.ico') else None,
    version='version_info.txt' if os.path.exists('version_info.txt') else None,
)
'''
    
    with open('BF3_License_Fixer.spec', 'w') as f:
        f.write(spec_content)
    
    print("✓ Spec file created: BF3_License_Fixer.spec")


def create_version_info():
    """Create version info file for Windows executable"""
    version_info = '''# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(1,2,0,0),
    prodvers=(1,2,0,0),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x40004,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Voidfnc (@voidfnc)'),
        StringStruct(u'FileDescription', u'BF3 License Fixer - Battlefield 3 License Activation Tool'),
        StringStruct(u'FileVersion', u'1.2.0.0'),
        StringStruct(u'InternalName', u'BF3_License_Fixer'),
        StringStruct(u'LegalCopyright', u'Copyright (C) 2025 Voidfnc. Licensed under MIT License.'),
        StringStruct(u'LegalTrademarks', u''),
        StringStruct(u'OriginalFilename', u'BF3_License_Fixer.exe'),
        StringStruct(u'ProductName', u'BF3 License Fixer'),
        StringStruct(u'ProductVersion', u'1.2.0'),
        StringStruct(u'Comments', u'Fixes "Could not activate license" error in EA App/Origin for Battlefield 3. Source: https://github.com/voidfnc/bf3-license-fixer'),
        StringStruct(u'PrivateBuild', u''),
        StringStruct(u'SpecialBuild', u'')])])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    
    with open('version_info.txt', 'w') as f:
        f.write(version_info)
    
    print("✓ Version info created: version_info.txt")


def create_assets_directory():
    """Create assets directory with placeholder files"""
    assets_dir = Path('assets')
    assets_dir.mkdir(exist_ok=True)
    
    # Create a simple icon file placeholder
    icon_path = assets_dir / 'icon.ico'
    if not icon_path.exists():
        print("ℹ Creating placeholder icon file")
        # For now, just create an empty file - in production you'd want a real icon
        icon_path.touch()
    
    print("✓ Assets directory prepared")


def build_executable():
    """Build the executable using PyInstaller"""
    print("\n🔨 Building executable...")
    
    # Clean previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
        print("✓ Cleaned previous dist directory")
    
    if os.path.exists('build'):
        shutil.rmtree('build')
        print("✓ Cleaned previous build directory")
    
    # Build using spec file
    try:
        subprocess.check_call([
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            'BF3_License_Fixer.spec'
        ])
        print("✅ Build completed successfully!")
        
        # Check if executable was created
        exe_path = Path('dist') / 'BF3_License_Fixer.exe'
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"📦 Executable created: {exe_path} ({size_mb:.1f} MB)")
        else:
            print("❌ Executable not found in expected location")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True


def create_installer_script():
    """Create NSIS installer script (optional)"""
    nsis_script = '''
; BF3 License Fixer Installer Script
; Requires NSIS (Nullsoft Scriptable Install System)

!define APP_NAME "BF3 License Fixer"
!define APP_VERSION "1.0.0"
!define APP_PUBLISHER "BF3 License Fixer Team"
!define APP_URL "https://github.com/your-repo/bf3-license-fixer"
!define APP_EXE "BF3_License_Fixer.exe"

Name "${APP_NAME}"
OutFile "BF3_License_Fixer_Setup.exe"
InstallDir "$PROGRAMFILES\\${APP_NAME}"
RequestExecutionLevel admin

Page directory
Page instfiles

Section "Install"
    SetOutPath "$INSTDIR"
    File "dist\\${APP_EXE}"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\\Uninstall.exe"
    
    ; Create start menu shortcut
    CreateDirectory "$SMPROGRAMS\\${APP_NAME}"
    CreateShortCut "$SMPROGRAMS\\${APP_NAME}\\${APP_NAME}.lnk" "$INSTDIR\\${APP_EXE}"
    CreateShortCut "$SMPROGRAMS\\${APP_NAME}\\Uninstall.lnk" "$INSTDIR\\Uninstall.exe"
    
    ; Create desktop shortcut
    CreateShortCut "$DESKTOP\\${APP_NAME}.lnk" "$INSTDIR\\${APP_EXE}"
    
    ; Registry entries for Add/Remove Programs
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "DisplayName" "${APP_NAME}"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "UninstallString" "$INSTDIR\\Uninstall.exe"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "Publisher" "${APP_PUBLISHER}"
    WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}" "DisplayVersion" "${APP_VERSION}"
SectionEnd

Section "Uninstall"
    Delete "$INSTDIR\\${APP_EXE}"
    Delete "$INSTDIR\\Uninstall.exe"
    RMDir "$INSTDIR"
    
    Delete "$SMPROGRAMS\\${APP_NAME}\\${APP_NAME}.lnk"
    Delete "$SMPROGRAMS\\${APP_NAME}\\Uninstall.lnk"
    RMDir "$SMPROGRAMS\\${APP_NAME}"
    
    Delete "$DESKTOP\\${APP_NAME}.lnk"
    
    DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\${APP_NAME}"
SectionEnd
'''
    
    with open('installer.nsi', 'w') as f:
        f.write(nsis_script)
    
    print("✓ NSIS installer script created: installer.nsi")
    print("ℹ To create installer, install NSIS and run: makensis installer.nsi")


def main():
    """Main build process"""
    print("🚀 BF3 License Fixer Build Script")
    print("=" * 40)
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Check if main_modern.py exists
    if not Path('main_modern.py').exists():
        print("❌ main_modern.py not found in current directory")
        return 1
    
    try:
        # Step 1: Check requirements
        print("\n1. Checking requirements...")
        check_requirements()
        
        # Step 2: Create build files
        print("\n2. Creating build files...")
        create_spec_file()
        create_version_info()
        create_assets_directory()
        
        # Step 3: Build executable
        print("\n3. Building executable...")
        if not build_executable():
            return 1
        
        # Step 4: Create installer script
        print("\n4. Creating installer script...")
        create_installer_script()
        
        print("\n✅ Build process completed successfully!")
        print("\nNext steps:")
        print("1. Test the executable in dist/BF3_License_Fixer.exe")
        print("2. Optionally create installer with NSIS using installer.nsi")
        print("3. Distribute the executable or installer")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Build failed with error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())