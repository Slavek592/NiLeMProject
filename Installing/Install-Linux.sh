#!/usr/bin/sh

echo This script can be used on Ubuntu and Ubuntu-like OS.
echo If You do not use this kind of Linux, press Ctrl+C.
read ready

echo This action will need root privileges to install the packages.
echo If You do not want to do it, press Ctrl+C.
read ready

echo Installing dependencies.

sudo apt-get install python3 python3-tk python3-pip
pip3 install tkPDFViewer

echo Congratulation! NiLeM is ready to be launched!

echo Starting installation.

SCRIPTDIR="$(dirname "$0")"
cd "$SCRIPTDIR"
cd ../

sudo mkdir /usr/share/NiLeM
sudo cp Installing/NiLeM-Linux.desktop /usr/share/applications/NiLeM.desktop
sudo cp -r NiLeM /usr/share/NiLeM/NiLeM
sudo cp -r Data /usr/share/NiLeM/Data
sudo cp -r Info /usr/share/NiLeM/Info
sudo cp -r Pictures /usr/share/NiLeM/Pictures
sudo cp NiLeM.py /usr/share/NiLeM/NiLeM.py
sudo cp NiLeM-Linux.sh /usr/share/NiLeM/NiLeM.sh

echo If there was no error, then congratulation! The NiLeM has been installed. Enjoy!
echo If You have succesfully installed NiLeM, You can delete any of the files in the NiLeMProject directory.
