#!/usr/bin/sh

if [ $(whoami) != "root" ]
  then echo "Please run as root"
  exit
fi

echo Installing dependencies.

apt-get install python3 python3-tk python3-pip
pip3 install tkPDFViewer

echo Congratulation! NiLeM is ready to be launched!
