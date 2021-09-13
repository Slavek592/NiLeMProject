#!/bin/sh
SCRIPTDIR="$(dirname "$0")"
cd "$SCRIPTDIR"
cd ../
echo This version uses tkinter for GUI. If You have not installed it, try running this command:
echo sudo apt-get install python3-tk
python3 NiLeSh/GraphicalNiLeSh.py

