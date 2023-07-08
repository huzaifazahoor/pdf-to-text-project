#!/bin/bash

# chmod +x ./script.sh
# ./script.sh

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Check if virtualenv is installed
if ! command -v virtualenv &>/dev/null; then
    echo "Virtualenv is not installed. Installing virtualenv..."
    pip3 install virtualenv
fi

# Check if Tesseract OCR is installed
if ! command -v tesseract &>/dev/null; then
    echo "Tesseract OCR is not installed. Installing Tesseract OCR..."
    brew install tesseract
fi

# Check if Tesseract language data is installed (optional)
if [ ! -d "/usr/local/Cellar/tesseract-lang" ]; then
    echo "Tesseract language data is not installed. Installing Tesseract language data..."
    brew install tesseract-lang
fi

# Create or activate the virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade -q pip

# Install requirements
echo "Installing requirements..."
pip3 install --upgrade -q -r requirements.txt

# Run main.py
echo "Running main.py..."
python3 main.py

# Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

echo "Script completed successfully."