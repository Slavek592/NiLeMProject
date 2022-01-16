#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Starting uninstallation.

rm /usr/local/share/applications/NiLeM.desktop
rm -r /usr/local/share/NiLeM

echo NiLeM has been uninstalled.
