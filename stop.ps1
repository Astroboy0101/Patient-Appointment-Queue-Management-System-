# Patient Queue System - Safe Shutdown Script (PowerShell)
# Stops all running servers and processes

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  PATIENT QUEUE SYSTEM - SHUTDOWN" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[STOP] Stopping all processes..." -ForegroundColor Yellow

# Stop Python processes
$pythonProcesses = Get-Process python -ErrorAction SilentlyContinue | Where-Object {
    $_.Path -like "*venv*" -or 
    $_.MainWindowTitle -like "*Patient*" -or 
    $_.MainWindowTitle -like "*Backend*" -or 
    $_.MainWindowTitle -like "*Frontend*" -or
    $_.MainWindowTitle -like "*Server*"
}

if ($pythonProcesses) {
    Write-Host "[STOP] Stopping Python processes..." -ForegroundColor Yellow
    $pythonProcesses | Stop-Process -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Python processes stopped" -ForegroundColor Green
} else {
    Write-Host "[INFO] No Python processes found" -ForegroundColor Cyan
}

# Free up ports 5000 and 8000
Write-Host "[STOP] Freeing up ports 5000 and 8000..." -ForegroundColor Yellow

$port5000 = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue
if ($port5000) {
    $port5000 | ForEach-Object {
        Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue
    }
}

$port8000 = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
if ($port8000) {
    $port8000 | ForEach-Object {
        Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "[OK] Ports freed" -ForegroundColor Green

# Wait a moment
Start-Sleep -Seconds 1

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  SHUTDOWN COMPLETE" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "All servers and processes have been stopped." -ForegroundColor Cyan
Write-Host ""

