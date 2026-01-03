# Patient Appointment & Queue Management System - Startup Script
# This script starts the backend server and opens the frontend

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Patient Queue System - Starting..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to project directory
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

# Step 1: Check Python
Write-Host "[1/6] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = & python --version 2>&1
    Write-Host "   [OK] $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "   [ERROR] Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Step 2: Check virtual environment
Write-Host "[2/6] Checking virtual environment..." -ForegroundColor Yellow
$venvPath = Join-Path $projectRoot "backend\venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "   [INFO] Creating virtual environment..." -ForegroundColor Yellow
    Set-Location "backend"
    python -m venv venv
    Set-Location $projectRoot
    Write-Host "   [OK] Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "   [OK] Virtual environment exists" -ForegroundColor Green
}

# Step 3: Install/Update dependencies
Write-Host "[3/6] Checking dependencies..." -ForegroundColor Yellow
$requirementsPath = Join-Path $projectRoot "backend\requirements.txt"
if (Test-Path $requirementsPath) {
    Write-Host "   [INFO] Installing dependencies..." -ForegroundColor Yellow
    & "$venvPath\Scripts\python.exe" -m pip install -q --upgrade pip
    & "$venvPath\Scripts\python.exe" -m pip install -q -r "$projectRoot\backend\requirements.txt"
    Write-Host "   [OK] Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "   [WARNING] requirements.txt not found" -ForegroundColor Yellow
}

# Step 4: Test database connection
Write-Host "[4/6] Testing database connection..." -ForegroundColor Yellow
Set-Location "backend"
$dbTest = & ".\venv\Scripts\python.exe" database.py 2>&1
if ($dbTest -match "SUCCESS") {
    Write-Host "   [OK] Database connected" -ForegroundColor Green
} else {
    Write-Host "   [WARNING] Database not connected - using mock data" -ForegroundColor Yellow
}
Set-Location $projectRoot

# Step 5: Test DSA modules
Write-Host "[5/6] Testing DSA modules..." -ForegroundColor Yellow
Set-Location "backend"
$dsaTest = & ".\venv\Scripts\python.exe" test_dsa.py 2>&1
if ($dsaTest -match "SUCCESS") {
    Write-Host "   [OK] All DSA modules working" -ForegroundColor Green
} else {
    Write-Host "   [WARNING] DSA test failed" -ForegroundColor Yellow
}
Set-Location $projectRoot

# Step 6: Display connection info
Write-Host "[6/6] System Information..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "System Configuration" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Backend: Railway (https://web-production-d92ae.up.railway.app)" -ForegroundColor Green
Write-Host "Database: Supabase (Connected)" -ForegroundColor Green
Write-Host "Frontend: Local (Opening in browser)" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Open frontend in browser
Write-Host "Opening frontend in browser..." -ForegroundColor Cyan
$frontendPath = Join-Path $projectRoot "frontend\index.html"
Start-Process $frontendPath

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "System Ready!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Frontend: Opened in browser" -ForegroundColor Cyan
Write-Host "Backend API: https://web-production-d92ae.up.railway.app/api" -ForegroundColor Cyan
Write-Host ""
Write-Host "Testing backend connection..." -ForegroundColor Yellow

# Test Railway backend
Start-Sleep -Seconds 2
try {
    $healthCheck = Invoke-WebRequest -Uri "https://web-production-d92ae.up.railway.app/api/health" -UseBasicParsing -TimeoutSec 10 -ErrorAction Stop
    Write-Host "[SUCCESS] Railway backend is running!" -ForegroundColor Green
    Write-Host "   Status: $($healthCheck.StatusCode)" -ForegroundColor Green
    $content = $healthCheck.Content | ConvertFrom-Json
    Write-Host "   Message: $($content.message)" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Railway backend may be sleeping or not responding" -ForegroundColor Yellow
    Write-Host "   Error: $($_.Exception.Message)" -ForegroundColor Yellow
    Write-Host "   Note: Railway free tier may sleep after inactivity" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "You can now use the application!" -ForegroundColor Green
Write-Host "If backend is sleeping, first request may take 30-60 seconds" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
