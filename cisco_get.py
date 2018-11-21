#!/usr/bin/env python

from netmiko import ConnectHandler
import sys


ip = sys.argv[1]
username = 'netmonitor'
password = 'Aa12345'

cisco = {'device_type':'cisco_ios', 'ip':ip,'username':username,'password':password} 

net_connect = ConnectHandler(**cisco)

results = net_connect.send_command("ping 114.114.114.114")
num = 0
for result in results:
	if result == '!':
		num += 1

print num
#ms = results.split("/")
