@echo off
REM ========================================
REM START APPLICATION ON RAILWAY
REM Opens the Railway deployment in browser
REM ========================================

title Patient Queue System - Railway

echo.
echo ========================================
echo   PATIENT QUEUE SYSTEM - RAILWAY
echo ========================================
echo.

cd /d "%~dp0"

echo [INFO] Opening Railway deployment...
echo.
echo Backend & Frontend: https://web-production-d92ae.up.railway.app
echo.
echo Opening in browser...
echo.

REM Open Railway URL in browser
start https://web-production-d92ae.up.railway.app

echo ========================================
echo   APPLICATION OPENED!
echo ========================================
echo.
echo The application is now running on Railway.
echo All features are available at:
echo   https://web-production-d92ae.up.railway.app
echo.
echo Press any key to exit...
pause >nul

