#!/usr/bin/sh

echo This action will need root privileges to install the packages.
echo If You do not want to do it, press Ctrl+C.
read ready

echo Installing dependencies.

sudo pkg install python38 x11-toolkits/py-tkinter databases/py-sqlite3 www/py-requests

echo Congratulation! NiLeM is ready to be launched!

echo Starting installation.

SCRIPTDIR="$(dirname "$0")"
cd "$SCRIPTDIR"
cd ../

sudo mkdir /usr/local/share/NiLeM
sudo cp Installing/NiLeM-FreeBSD.desktop /usr/local/share/applications/NiLeM.desktop
sudo cp -r NiLeM /usr/local/share/NiLeM/NiLeM
sudo cp -r Data /usr/local/share/NiLeM/Data
sudo cp -r Info /usr/local/share/NiLeM/Info
sudo cp -r Pictures /usr/local/share/NiLeM/Pictures
sudo cp NiLeM.py /usr/local/share/NiLeM/NiLeM.py
sudo cp NiLeM-FreeBSD.sh /usr/local/share/NiLeM/NiLeM.sh

echo If there was no error, then congratulation! The NiLeM has been installed. Enjoy!
echo If You have succesfully installed NiLeM, You can delete any of the files in the NiLeMProject directory.
