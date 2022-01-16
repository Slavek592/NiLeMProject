#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting uninstallation.

rm /usr/share/applications/NiLeM.desktop
rm -r /usr/share/NiLeM

echo NiLeM has been uninstalled.
