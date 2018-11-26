#!/usr/bin/env python

from netmiko import ConnectHandler
import sys 
import os


username = 'netmonitor'
password = 'Aa12345'

def ssh_cisco_to_run_ping(ip_address, username, password):
	cisco = {'device_type':'cisco_ios', 'ip':ip_address,'username':username,'password':password}
	net_connect = ConnectHandler(**cisco)
	results = net_connect.send_command("ping 114.114.114.114")
	packet_available = 0
	for result in results:
		if result == '!':
			packet_available += 1
	return packet_available

