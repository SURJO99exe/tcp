@echo off
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)
echo Virtual environment created successfully!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
pause
