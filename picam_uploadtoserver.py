#!/usr/bin/python

from datetime import datetime
from urllib import urlretrieve
from time import gmtime, strftime, mktime
import os
import time
import socket
import httplib
import requests
import glob
import sys
import ast

c = open('config_location.txt','r')
config_loc = c.readline().strip()
c.close()

f = open(config_loc+'id.txt','r')
id = (f.readline()).strip()
p = '{\'id\': \"'+id+'\"}'
payload = ast.literal_eval(p)
f.close()

g = open(config_loc+'server.txt','r')
url = g.readline().strip()
g.close()

s = open(config_loc+'pingserver.txt','r')
pingurl = s.readline().strip()
s.close()

uuid = "".join("{:02x}".format(ord(c)) for c in id)
pingpayload = "id="+id + "&uuid=" + uuid


print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": starting application"

while True:

    if (int(time.mktime(datetime.utcnow().timetuple())) % 60) == 0:
        time.sleep(1)
        try:
            print "------------------------------------------------------------------------------------------"
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Sending ping to server"
        
            r = requests.post(pingurl, data=pingpayload, timeout = 5)
            response2 = str(r.json)
            if (response2.find("200") > 0):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Got a 200 from server, ping successful"
            else:
                print response2
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Bad response from server, ping failed"
            
            print "------------------------------------------------------------------------------------------"
    
        except:
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:", sys.exc_info()[0]
            print "------------------------------------------------------------------------------------------"
            continue
    
    try:
        listOfFiles = glob.glob("*_image.jpg")
        if len(listOfFiles) > 0:
            print "------------------------------------------------------------------------------------------"
            fileToSend = listOfFiles[0]
            print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Sending image to server ["+fileToSend+"]"
            
            files = {'images[]':open(fileToSend)} #'file' => name of html input field
            r = requests.post(url, data=payload, files=files, timeout = 5)
            response2 = str(r.json)
            if (response2.find("200") > 0):
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Got a 200 from server, image upload successful"
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Deleting Image"
                os.remove(fileToSend)
            else:
                print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Bad response from server, image upload failed"
            
            print "------------------------------------------------------------------------------------------"
    except:
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())+": Unexpected error:", sys.exc_info()[0]
        print "------------------------------------------------------------------------------------------"
        continue

