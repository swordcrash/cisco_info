#!/usr/bin/env python3
# zabbix script
# reading /tmp/xxx for ping response time

import os 
import sys


ip = sys.argv[1]
URL = sys.argv[2]
res_file = "/tmp/" + URL +"_res_" + ip
fo = open(res_file, 'r')
line = fo.readline()
line = int(line)
print (line)
