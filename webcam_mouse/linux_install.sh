#!/bin/sh

echo Updating System
sudo apt-get update
sudo apt-get upgrade

echo Getting prereq
sudo apt-get install build-essential cmake git pkg-config
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libatlas-base-dev gfortran

echo Installing pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

echo Installing prereq
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
mkvirtualenv cv
sudo apt-get install git

echo Installing Python, Numpy, OpenCV
sudo apt-get install python2.7-dev
pip install numpy
cp install/opencv/x86/cv2.pyd /usr/local/lib/python2.7/site-packages/cv2.pyd