#!/bin/bash

# Checking for Python 3 installation
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
    python3 --version # Displays the Python version
else
    echo "Python 3 is not installed"
    echo "Run install_python.sh to install Python 3." # Give user the option to install Python 3
fi