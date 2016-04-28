
> enable camera
	- sudo raspi-config
	- menu 5 (enable camera)
	- confirm
  	- finish
  	- reboot

> update OS
	- sudo apt-get update 
	- sudo apt-get upgrade

> copy over picam folder into /home/pi folder

> install requests
	- cd requests
	- sudo python setup.py install

> focus camera
	- python picam_focus.py <length of preview in ms> (ex: python picam_focus.py 10000)

> configure the id, and interval in the "config_files" folder

> if you want to move the config folder, just adjust its path in the "config_location.txt" file

> run each script for a few seconds to make sure they work
	- cd picam/
	- chmod 755 uploadlauncher.sh
	- chmod 755 downloadlauncher.sh
	- ./downloadlauncher.sh
	- ./uploadlauncher.sh

> setup cron job to launch on startup (if needed)
	- sudo crontab -e (place following lines at the bottom)
		> @reboot sh /home/pi/picam/downloadlauncher.sh >/home/pi/picam/logs/cronlog 2>&1
		> @reboot sh /home/pi/picam/uploadlauncher.sh >/home/pi/picam/logs/cronlog 2>&1



