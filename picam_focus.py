#!/usr/bin/python

import os
import sys

sys.path.insert(0, "usr/bin/raspistill")

try:
    if len(sys.argv) == 2:
        os.system('raspistill -t '+str(sys.argv[1])+' -p 100,100,900,600')
    else:
        os.system('raspistill -t 1000 -p 100,100,900,600')

except:
    error = str(sys.exc_info()[0])
    print "Unexpected error:"+ error