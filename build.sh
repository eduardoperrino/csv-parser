#!/bin/bash

# Script base name (i.e. script name minus .py extension)
scriptBaseName=parserBuilder

# First check for PyInstaller
command -v pyinstaller >/dev/null 2>&1 || {
    echo >&2 "PyInstaller is required to build the executable.";
    echo >&2 "Please install PyInstaller with:";
    echo >&2 "  (sudo) pip install pyinstaller"
    exit 1;
}

pyinstaller --onefile parser.py 2> /dev/null

if [ $? -eq 0 ]
then
  echo "Successfully created binary file at dist folder"
else
  echo "Could not create file" >&2
fi
