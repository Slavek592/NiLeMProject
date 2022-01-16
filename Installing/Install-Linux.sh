#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting installation.

SCRIPTDIR="$(dirname "$0")"
cd "$SCRIPTDIR"
cd ../

mkdir /usr/share/NiLeM
cp Installing/NiLeM-Linux.desktop /usr/share/applications/NiLeM.desktop
cp -r NiLeM /usr/share/NiLeM/NiLeM
cp -r Data /usr/share/NiLeM/Data
cp -r Info /usr/share/NiLeM/Info
cp -r Pictures /usr/share/NiLeM/Pictures
cp NiLeM.py /usr/share/NiLeM/NiLeM.py
cp NiLeM-Linux.sh /usr/share/NiLeM/NiLeM.sh
mkdir /usr/share/NiLeM/NileshScripts
chmod 777 /usr/share/NiLeM/NileshScripts

echo Congratulation! The NiLeM has been installed. Enjoy!
echo If there is a problem, try installing dependencies.
echo If You have succesfully installed NiLeM, You can delete any of the files in the NiLeMProject directory.
