@echo off
echo ===============================================
echo BF3 License Fixer - Setup Dependencies
echo ===============================================
echo.

echo Checking Python installation...
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed or not in PATH!
        echo Please install Python 3.8+ from python.org and add it to your PATH.
        echo.
        echo To add Python to PATH:
        echo 1. Search for "Environment Variables" in Windows
        echo 2. Click "Environment Variables" button
        echo 3. Under "System Variables", find and select "Path"
        echo 4. Click "Edit" and add your Python installation directory
        echo 5. Restart Command Prompt and try again
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo ✓ Python found and accessible via PATH
%PYTHON_CMD% --version

echo.
echo Installing/Updating required packages...
echo.

echo [1/3] Installing PyInstaller...
%PYTHON_CMD% -m pip install --upgrade pyinstaller

echo [2/3] Installing psutil...
%PYTHON_CMD% -m pip install --upgrade psutil

echo [3/3] Installing Pillow...
%PYTHON_CMD% -m pip install --upgrade pillow

echo.
echo ✓ Setup complete! You can now run build_modern.bat
pause
