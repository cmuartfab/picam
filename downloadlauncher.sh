#!/bin/sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/picam/
while :
do
	sudo python picam_downloadfromcamera.py
done
cd /