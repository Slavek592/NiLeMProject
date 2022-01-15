#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting uninstallation.

rm /usr/share/applications/NiLeM.desktop
rm -r /usr/share/NiLeM/NiLeM
rm -r /usr/share/NiLeM/Data
rm -r /usr/share/NiLeM/Info
rm -r /usr/share/NiLeM/Pictures
rm /usr/share/NiLeM/NiLeM.py
rm /usr/share/NiLeM/NiLeM.sh
rmdir /usr/share/NiLeM

echo NiLeM has been uninstalled.
