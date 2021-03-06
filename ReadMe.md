# picam

**picam** is a Raspberry Pi stop motion camera used to create zoomable time-elapse video based on the ECam from CMU Create Lab.

## Bug Reports and Discussion
Please use the [GitHub Issue Tracker](https://github.com/cmuartfab/ml-lib/issues) for all bug reports and feature requests.

Please use the [ArtFab Discussion form (under Software \> ml.lib)](http://discuss.artfab.art.cmu.edu/c/software/ml-lib) for all general conversations, questions, discussions and project sharing.  

## Installation
- Download the latest Raspbian from [Raspbian download page](https://www.raspberrypi.org/downloads/raspbian/)
- Follow the [installation guide](http://raspberrypi.org/documentation/installation/installing-images/README.md) for your operation system.
- Note: Follow the installation guide instead of using NOOBS for this software. 

## Assembly
- Carefully assemble the camera to the RPi. Make sure the blue tape side is towards the Ethernet port.
- Video tutorial [here](https://www.raspberrypi.org/help/camera-module-setup/)
- Plugin keyboard, mouse and monitor if necessary.
- Plugin the SD card and power your pi.

## General Operation
- Keyboard, mouse and monitor is a good way to start with limited knowledge of linux system or command line. 
- For experienced users, try SSH in with its IP address, or connect the RPi with your desktop/laptop via Ethernet port to use .local domain. See [here](http://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/)

## Picam 
> Enable camera 
- `sudo raspi-config`
- Choose “Enable Camera” 
- Confirm
- Finish
- [sudo reboot](#) 

> update apt-get
- `sudo apt-get update`
- `sudo apt-get upgrade`

> install picam
- clone this repository or download the [zip file](https://github.com/cmuartfab/picam/archive/master.zip)
- rename "picam-master" to "picam" if necessary; copy folder into /home/pi folder on the raspberry pi

> install python package dependencies
- `cd /home/pi/picam/requests`
- `sudo python setup.py install`

> focus camera
- python picam_focus.py \<length of preview in ms\> 
	(ex: `python picam_focus.py 10000`)

> configure the camera ID and the snapshot interval; all config files are in "/home/pi/picam/config_files" 
- `sudo nano id.txt`: change ID
- `sudo nano interval.txt`: change intervael
-  NOTE: if you want to move the config folder, just adjust its path in the "config_location.txt" file


> change permissions on the shell scripts to make the executable
- `cd /home/pi/picam/`
- `chmod 755 uploadlauncher.sh`
- `chmod 755 downloadlauncher.sh`

> run each script for a few seconds to make sure they work
- `cd /home/pi/picam/`
- `./downloadlauncher.sh`
- `./uploadlauncher.sh`

> setup cron job to launch on startup (if needed)
- `sudo crontab -e`
- place following lines at the bottom
- `@reboot sh /home/pi/picam/downloadlauncher.sh \>/home/pi/picam/logs/cronlog 2\>&1`
- `@reboot sh /home/pi/picam/uploadlauncher.sh \>/home/pi/picam/logs/cronlog 2\>&1`
