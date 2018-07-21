#!/bin/bash

echo "Creating virtual environment:"
PYTHON=/usr/bin/python3.4
if [ ! -x $PYTHON ]; then
  PYTHON=/usr/bin/python;
fi
echo "using python: $PYTHON"
virtualenv -p $PYTHON venv

echo "Activate virtual environment:"
source ~/workspace/venv/bin/activate

echo "Installing requirements:"
pip install -r dev-requirements.txt

echo "Environment setup completed!"
echo "======================================"
echo "To activate virtual environment, run:"
echo "source ~/workspace/venv/bin/activate"
echo "======================================"

