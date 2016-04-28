#!/bin/sh

cd /
cd home/pi/picam/
while :
do
	sudo python picam_uploadtoserver.py
done
cd /