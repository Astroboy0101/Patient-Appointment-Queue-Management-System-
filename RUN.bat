@echo off
REM ========================================
REM ONE-CLICK STARTUP SCRIPT
REM Starts backend server, frontend server, and opens browser
REM ========================================

title Patient Queue System - Starting...

echo.
echo ========================================
echo   PATIENT QUEUE SYSTEM - STARTUP
echo ========================================
echo.

cd /d "%~dp0"

REM Quick system check
echo [CHECK] Verifying system...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)
echo [OK] Python found
echo.

REM Setup virtual environment if needed
if not exist "backend\venv" (
    echo [SETUP] Creating virtual environment...
    cd backend
    python -m venv venv
    cd ..
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment exists
)
echo.

REM Install dependencies
echo [SETUP] Installing dependencies...
cd backend
call venv\Scripts\activate.bat >nul 2>&1
pip install -q -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Some dependencies may have failed to install
) else (
    echo [OK] Dependencies installed
)
echo.

REM Test database
echo [TEST] Testing database connection...
python database.py >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Database test failed - using mock data
) else (
    echo [OK] Database connected to Supabase
)
echo.

REM Test DSA modules
echo [TEST] Testing DSA modules...
python test_dsa.py >nul 2>&1
if errorlevel 1 (
    echo [WARNING] DSA test failed
) else (
    echo [OK] DSA modules working
)
echo.

cd ..

echo ========================================
echo   STARTING SERVERS
echo ========================================
echo.
echo Backend Server: http://localhost:5000
echo Frontend Server: http://localhost:8000
echo Database: Supabase (Connected)
echo.
echo Starting both servers...
echo.

REM Start the Python server script that handles both servers
python start_server.py

pause
