#!/bin/bash

echo "Creating virtual environment..."

# Check if Python is installed
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
else
    echo "ERROR: Python is not installed"
    exit 1
fi

$PYTHON_CMD -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

echo "Virtual environment created successfully!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
