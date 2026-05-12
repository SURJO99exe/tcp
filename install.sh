#!/bin/bash

echo "========================================"
echo "SURJO LIVE TCP BOT - Linux/Termux Setup"
echo "========================================"
echo ""

# Check if Python is installed
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "ERROR: Python is not installed"
    if [ -n "$TERMUX_VERSION" ]; then
        echo "Installing Python via pkg..."
        pkg install python -y
        PYTHON_CMD=python
    else
        echo "Please install Python 3.8 or higher"
        exit 1
    fi
fi

echo "[1/5] Creating virtual environment..."
$PYTHON_CMD -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Upgrading pip..."
pip install --upgrade pip

echo "[4/5] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[5/5] Setup complete!"
echo ""
echo "========================================"
echo "SETUP COMPLETED SUCCESSFULLY!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Create 'SURJO LIVE.txt' file with your credentials"
echo "2. Run: python main.py"
echo ""
echo "To activate virtual environment in future:"
echo "  source venv/bin/activate"
echo ""