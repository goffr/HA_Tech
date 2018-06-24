#!/usr/bin/python
#Place in /usr/local/bin/TV_Power-Samsung_On.py

import sys
import os
import time
import urllib2

#Domoticz Method

local_server = ''; #enter a local address that would resolve when network is operational
domoticz_server = '';  #enter domticz server ip address here
domoticz_port = '';  #enter domoticz server port here
username = "";  #enter domoticz username here
password = "";  #enter domoticz password here
idx = '';  #enter idx here

def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://" + testurl/index.html',timeout=1)
            return
        except urllib2.URLError:
            pass
            
def updateDomoticz(idx, statusval):
#   time.sleep(1) # Delay if necessary
#   logger.info("Updating Status: " + statusval + ", ID: " + str(idx))
   os.system("/usr/bin/curl -m 10 -s 'http://" + username + ":" + password + "@" + domoticz_server + ":" + domoticz_por$

wait_for_internet_connection()  #necessary upon startup if network is unavailable before script runs
updateDomoticz(idx, "On")

#Direct Method
#os.system("irsend -a 192.168.10.95:8765 SEND_ONCE vizio KEY_POWER")
