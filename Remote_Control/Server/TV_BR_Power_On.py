#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import sys
import logging
import datetime
import time
from time import sleep

#create logger
logger = logging.getLogger("EventSvr")
logger.setLevel(logging.DEBUG)
#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#add formatter to ch
ch.setFormatter(formatter)
#add ch to logger
logger.addHandler(ch)

#"application" code
#logger.debug("debug message")
#logger.info("info message")
#logger.warn("warn message")
#logger.error("error message")
#logger.critical("critical message")

HOST = ''   # ip address of TV control RPi
PORT = '' # Arbitrary non-privileged port

def sendMessage(rcvHost, realmsg):
  logger.info("Send to Address: " + rcvHost + ", Message: " + realmsg)
  # create dgram udp socket
  try:
    s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  except socket.error:
    logger.error('Failed to create socket')
  tempHost = rcvHost;
  tempPort = PORT;
  try :
    #Set the whole string
    s2.sendto(realmsg, (tempHost, tempPort))

    # receive data from client (data, addr)
    da = s2.recvfrom(1024)
    reply = da[0]
    addr = da[1]

    logger.info('Server reply : ' + reply)

  except socket.error, msg:
    logger.error('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

#RUN

sendMessage(HOST, "TV_ON")

exit()
