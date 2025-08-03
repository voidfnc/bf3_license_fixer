#!/usr/bin/env python3
"""
Create version info file for BF3 License Fixer
"""

import sys
from pathlib import Path

def create_version_info():
    """Create a properly formatted version info file"""
    version_info_content = """VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1,2,0,0),
    prodvers=(1,2,0,0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
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
        StringStruct(u'OriginalFilename', u'BF3_License_Fixer.exe'),
        StringStruct(u'ProductName', u'BF3 License Fixer'),
        StringStruct(u'ProductVersion', u'1.2.0'),
        StringStruct(u'Comments', u'Fixes EA App/Origin license error for Battlefield 3. GitHub: https://github.com/voidfnc/bf3-license-fixer')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)"""
    
    # Write to version_info.txt
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_info_content)
    
    print("✓ Created version_info.txt")

if __name__ == '__main__':
    create_version_info()
