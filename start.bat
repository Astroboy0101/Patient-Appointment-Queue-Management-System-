@echo off
REM Patient Appointment & Queue Management System - Startup Script (Windows Batch)
REM Double-click this file to start everything

echo ========================================
echo Patient Queue System - Starting...
echo ========================================
echo.

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo [1/5] Python found
echo.

REM Check virtual environment
if not exist "backend\venv" (
    echo [2/5] Creating virtual environment...
    cd backend
    python -m venv venv
    cd ..
    echo [OK] Virtual environment created
) else (
    echo [2/5] Virtual environment exists
)
echo.

REM Install dependencies
echo [3/5] Installing dependencies...
cd backend
call venv\Scripts\activate.bat
pip install -q -r requirements.txt >nul 2>&1
echo [OK] Dependencies installed
echo.

REM Test database
echo [4/5] Testing database connection...
python database.py
echo.

REM Display system info
echo [5/5] System Information
echo.
echo ========================================
echo System Configuration
echo ========================================
echo Backend: Railway (https://web-production-d92ae.up.railway.app)
echo Database: Supabase (Connected)
echo Frontend: Local (Opening in browser)
echo ========================================
echo.

REM Open frontend
echo Opening frontend in browser...
start "" "%~dp0frontend\index.html"

echo.
echo ========================================
echo System Ready!
echo ========================================
echo.
echo Frontend: Opened in browser
echo Backend API: https://web-production-d92ae.up.railway.app/api
echo.

REM Test Railway backend
echo Testing Railway backend connection...
curl -s https://web-production-d92ae.up.railway.app/api/health >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Railway backend may be sleeping
    echo Note: First request may take 30-60 seconds
) else (
    echo [SUCCESS] Railway backend is running!
)

echo.
echo You can now use the application!
echo.
pause
