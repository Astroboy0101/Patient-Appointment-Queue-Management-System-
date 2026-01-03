#!/bin/bash
# Patient Appointment & Queue Management System - Startup Script (Linux/Mac)
# Run: chmod +x start.sh && ./start.sh

echo "========================================"
echo "Patient Queue System - Starting..."
echo "========================================"
echo ""

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check Python
echo "[1/6] Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "   [ERROR] Python 3 not found. Please install Python 3.8+"
    exit 1
fi
echo "   [OK] Python found"
echo ""

# Check virtual environment
echo "[2/6] Checking virtual environment..."
if [ ! -d "backend/venv" ]; then
    echo "   [INFO] Creating virtual environment..."
    cd backend
    python3 -m venv venv
    cd ..
    echo "   [OK] Virtual environment created"
else
    echo "   [OK] Virtual environment exists"
fi
echo ""

# Install dependencies
echo "[3/6] Installing dependencies..."
cd backend
source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "   [OK] Dependencies installed"
echo ""

# Test database
echo "[4/6] Testing database connection..."
python database.py
echo ""

# Test DSA modules
echo "[5/6] Testing DSA modules..."
python test_dsa.py
echo ""

# Start backend
echo "[6/6] Starting backend server..."
echo ""
echo "========================================"
echo "Backend Server Starting..."
echo "Server will run on: http://localhost:5000"
echo "========================================"
echo ""
echo "Opening frontend in browser..."
echo ""

# Open frontend (Linux)
if command -v xdg-open &> /dev/null; then
    xdg-open frontend/index.html &
elif command -v open &> /dev/null; then
    open frontend/index.html &
fi

# Start backend
python app.py


