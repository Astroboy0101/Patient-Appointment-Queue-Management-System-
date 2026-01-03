@echo off
REM ========================================
REM SAFE SHUTDOWN SCRIPT
REM Stops all running servers and processes
REM ========================================

title Patient Queue System - Shutting Down...

echo.
echo ========================================
echo   PATIENT QUEUE SYSTEM - SHUTDOWN
echo ========================================
echo.

echo [STOP] Stopping all processes...

REM Stop Python processes related to the project
tasklist /FI "IMAGENAME eq python.exe" 2>nul | find /I "python.exe" >nul
if %ERRORLEVEL% == 0 (
    echo [STOP] Stopping Python processes...
    for /f "tokens=2" %%a in ('tasklist /FI "IMAGENAME eq python.exe" /FO LIST ^| findstr /I "PID"') do (
        taskkill /F /PID %%a >nul 2>&1
    )
    echo [OK] Python processes stopped
) else (
    echo [INFO] No Python processes found
)

REM Stop processes on ports 5000 and 8000
echo [STOP] Freeing up ports 5000 and 8000...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":5000"') do (
    taskkill /F /PID %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000"') do (
    taskkill /F /PID %%a >nul 2>&1
)
echo [OK] Ports freed

REM Stop any windows with "Patient" or "Server" in title
echo [STOP] Closing application windows...
taskkill /FI "WINDOWTITLE eq *Patient*" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq *Backend*" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq *Frontend*" /F >nul 2>&1
echo [OK] Windows closed

echo.
echo ========================================
echo   SHUTDOWN COMPLETE
echo ========================================
echo.
echo All servers and processes have been stopped.
echo.
echo Press any key to exit...
pause >nul

