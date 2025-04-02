#!/bin/bash

# Set src as a Python module path
export PYTHONPATH=src

# Run your main script
python3 main.py

# Start server in the public folder
cd public
python3 -m http.server
