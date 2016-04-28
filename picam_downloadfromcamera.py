#!/usr/bin/python

from datetime import datetime
from time import gmtime, strftime, mktime
import os
import time
import sys


c = open('config_location.txt','r')
config_loc = c.readline().strip()
c.close()

i = open(config_loc+'interval.txt','r')
interval = int(i.readline().strip())
i.close()

print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": starting application"
while True:

    curDate = str(int(time.mktime(datetime.utcnow().timetuple())))
    
    if (int(time.mktime(datetime.utcnow().timetuple())) % interval) == 0:
        try:
            print "******************************************************************************************"
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": taking picture"
            
            imageName = curDate+'_img'+'.jpg'
            imageDoneName = curDate+'_image'+'.jpg'
            
            os.system('raspistill -o ' + imageName + ' -t 1 -n')

            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": picture saved ["+imageName+"]"
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": picture renamed ["+imageDoneName+"]"
            os.rename(imageName,imageDoneName)
        
            print "******************************************************************************************"
    
        except:
            error = str(sys.exc_info()[0])
            
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:"+ error
            print "******************************************************************************************"
            continue

