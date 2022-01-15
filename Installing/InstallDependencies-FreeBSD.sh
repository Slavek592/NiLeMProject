#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Installing dependencies.

sudo pkg install python38 x11-toolkits/py-tkinter databases/py-sqlite3 www/py-requests

echo Congratulation! NiLeM is ready to be launched!
