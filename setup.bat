@echo off
echo ========================================
echo SURJO LIVE TCP BOT - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/5] Upgrading pip...
python -m pip install --upgrade pip

echo [4/5] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [5/5] Setup complete!
echo.
echo ========================================
echo SETUP COMPLETED SUCCESSFULLY!
echo ========================================
echo.
echo Next steps:
echo 1. Create 'SURJO LIVE.txt' file with your credentials
echo 2. Run: python main.py
echo.
echo To activate virtual environment in future:
echo   venv\Scripts\activate.bat
echo.
pause
