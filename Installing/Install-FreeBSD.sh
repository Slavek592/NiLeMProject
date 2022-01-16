#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting installation.

SCRIPTDIR="$(dirname "$0")"
cd "$SCRIPTDIR"
cd ../

mkdir /usr/local/share/NiLeM
cp Installing/NiLeM-FreeBSD.desktop /usr/local/share/applications/NiLeM.desktop
cp -r NiLeM /usr/local/share/NiLeM/NiLeM
cp -r Data /usr/local/share/NiLeM/Data
chmod -R 777 /usr/local/share/NiLeM/Data
cp -r Info /usr/local/share/NiLeM/Info
cp -r Pictures /usr/local/share/NiLeM/Pictures
cp NiLeM.py /usr/local/share/NiLeM/NiLeM.py
cp NiLeM-FreeBSD.sh /usr/local/share/NiLeM/NiLeM.sh
mkdir /usr/local/share/NiLeM/NileshScripts
chmod 777 /usr/local/share/NiLeM/NileshScripts

echo Congratulation! The NiLeM has been installed. Enjoy!
echo If there is a problem, try installing dependencies.
echo If You have succesfully installed NiLeM, You can delete any of the files in the NiLeMProject directory.
