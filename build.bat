@echo off
echo ===============================================
echo BF3 License Fixer - Build Script
echo ===============================================
echo.

:: Check if Python is installed and accessible
echo [1/6] Checking Python installation...
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed or not in PATH!
        echo Please install Python 3.8+ and add it to your PATH.
        echo Run setup.bat first to install dependencies.
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo ✓ Python found and accessible
%PYTHON_CMD% --version

:: Check if required files exist
echo.
echo [2/6] Checking required files...

if not exist "main_modern.py" (
    echo ERROR: main_modern.py not found!
    pause
    exit /b 1
)
echo ✓ main_modern.py found

if not exist "themes" (
    echo ERROR: themes directory not found!
    pause
    exit /b 1
)
echo ✓ themes directory found

if exist "app_icon.ico" (
    echo ✓ app_icon.ico found - will include icon
) else (
    echo WARNING: app_icon.ico not found - building without icon
)

if exist "version_info.txt" (
    echo ✓ version_info.txt found - will include metadata
) else (
    echo ℹ version_info.txt will be auto-generated
)

:: Check if required packages are installed
echo.
echo [3/6] Checking dependencies...

echo Checking PyInstaller...
%PYTHON_CMD% -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    %PYTHON_CMD% -m pip install pyinstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller!
        pause
        exit /b 1
    )
) else (
    echo ✓ PyInstaller is installed
)

echo Checking psutil...
%PYTHON_CMD% -m pip show psutil >nul 2>&1
if errorlevel 1 (
    echo Installing psutil...
    %PYTHON_CMD% -m pip install psutil
    if errorlevel 1 (
        echo ERROR: Failed to install psutil!
        pause
        exit /b 1
    )
) else (
    echo ✓ psutil is installed
)

echo Checking Pillow...
%PYTHON_CMD% -m pip show pillow >nul 2>&1
if errorlevel 1 (
    echo Installing pillow...
    %PYTHON_CMD% -m pip install pillow
    if errorlevel 1 (
        echo ERROR: Failed to install Pillow!
        pause
        exit /b 1
    )
) else (
    echo ✓ Pillow is installed
)

echo.
echo [4/6] Cleaning previous builds...
if exist "build" (
    echo Removing build directory...
    rmdir /s /q "build"
)
if exist "dist" (
    echo Removing dist directory...
    rmdir /s /q "dist"
)

echo.
echo [5/6] Building BF3 License Fixer...
echo Creating version info file with @voidfnc attribution...
%PYTHON_CMD% create_version_info.py

echo Using spec file: BF3_License_Fixer.spec
%PYTHON_CMD% -m PyInstaller --clean BF3_License_Fixer.spec

if errorlevel 1 (
    echo.
    echo ERROR: PyInstaller build failed!
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo [6/6] Build complete!
echo.

:: Test if executable was created
if exist "dist\BF3_License_Fixer.exe" (
    echo ✓ SUCCESS: BF3 License Fixer executable built successfully!
    for %%A in ("dist\BF3_License_Fixer.exe") do (
        echo   File size: %%~zA bytes (~20 MB)
    )
    echo   Location: %CD%\dist\BF3_License_Fixer.exe
    echo.
    echo Features included:
    if exist "app_icon.ico" (
        echo   ✓ Custom application icon
    )
    echo   ✓ Version information and metadata
    echo   ✓ Author: @voidfnc
    echo   ✓ Anti-virus friendly metadata
    echo   ✓ Modern themed GUI
    echo   ✓ Complete themes bundle
    echo   ✓ All dependencies included
    echo.
    echo You can now distribute the executable:
    echo   dist\BF3_License_Fixer.exe
    echo.
    echo The executable includes professional metadata to avoid
    echo false positives from antivirus software.
) else (
    echo ✗ ERROR: Build failed - executable was not created!
    echo.
    echo Troubleshooting:
    echo 1. Check if main_modern.py exists in current directory
    echo 2. Check if themes folder exists
    echo 3. Check if BF3_License_Fixer.spec exists
    echo 4. Look for error messages above
    echo 5. Try running: %PYTHON_CMD% main_modern.py
)

echo.
echo Build process completed!
echo Press any key to exit...
pause >nul
