#!/usr/bin/env python3
# zabbix script
# reading /tmp/xxx for ping test

import os 
import sys


ip = sys.argv[1]
URL = sys.argv[2]
ping_file = "/tmp/" + URL +"_ping_" + ip
fo = open(ping_file, "r")
line = fo.readline()
line = int(line)
print (line)
