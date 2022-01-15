#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting uninstallation.

rm /usr/local/share/applications/NiLeM.desktop
rm -r /usr/local/share/NiLeM/NiLeM
rm -r /usr/local/share/NiLeM/Data
rm -r /usr/local/share/NiLeM/Info
rm -r /usr/local/share/NiLeM/Pictures
rm /usr/local/share/NiLeM/NiLeM.py
rm /usr/local/share/NiLeM/NiLeM.sh
rmdir /usr/local/share/NiLeM

echo NiLeM has been uninstalled.
