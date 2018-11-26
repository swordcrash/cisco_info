#!/usr/bin/env python

import os
import time
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from cisco_ping import ssh_cisco_to_run_ping 
#logging.basicConfig()
"""
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
"""

def get_ping():
	ip_list = [
		"10.33.84.1",
		"10.33.92.1",
		"10.33.88.1",
		"10.33.104.1",
		"10.33.53.1",
		"10.33.33.1",
		"10.33.29.1",
		"10.33.49.1",
		"10.33.42.1",
		"10.33.132.1"
	]
	print ip_list
	username = 'netmonitor'
	password = 'Aa12345'
	flag = 0
	for ip in ip_list:
		print ip
		res = ssh_cisco_to_run_ping(ip, username, password)
		ping_file = "/tmp/ping_" + ip
		os.system("echo " + str(res) + " > " + ping_file)
		flag += 1
	return flag

def putout():
	print "x"

def main():
	sched = BlockingScheduler()
	sched.add_job(get_ping, 'interval', seconds=60) 
	#sched.add_job(putout, 'interval', seconds=3) 
	#sched.add_job(available_report_daily, 'cron', day_of_week='0-6', hour=6, minute=5, end_date='2046-05-01')
	#sched.add_job(available_report_weekly, 'cron', day_of_week='sat', hour=9, minute=0, end_date='2046-05-01')
	#sched.add_job(available_report_daily, 'cron', day_of_week='0-6', hour=9, minute=40, end_date='2046-05-01')
	sched.start()

if __name__ == "__main__": 
	main()
