@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Python is not installed. Installing Python...
    winget install Python
)

REM Check if the virtual environment folder 'env' exists, and create it if not
if not exist env (
    python -m venv env
    echo Virtual environment 'env' created.
)

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install Python dependencies from requirements.txt
echo Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% NEQ 0 (
    echo Failed to install Python dependencies. Exiting...
    exit /b 1
)

echo All dependencies are installed.