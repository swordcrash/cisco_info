#!/usr/bin/env python

import os 
import sys


ip = sys.argv[1]
ping_file = "/tmp/ping_" + ip
os.system("cat " + ping_file)
