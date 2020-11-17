#!/usr/bin/env python3
# zabbix script
# running on backgroud to get result from cisco, save the results in /tmp
#

import os
import time
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
#from cisco_ping import ssh_cisco_to_run_ping 
from cisco_check import ssh_cisco_to_run_ping 
#logging.basicConfig()
"""
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
"""

# the old version 
def get_ping_cdc():
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
        "10.33.136.1",
        "10.33.128.1",
        "10.33.132.1"
    ]
    print (ip_list)
    username = ''
    password = ''
    flag = 0
    for ip in ip_list:
        print (ip)
        res = ssh_cisco_to_run_ping(ip, username, password)
        ping_file = "/tmp/ping_" + ip
        os.system("echo " + str(res) + " > " + ping_file)
        flag += 1
    return flag

# test network quality: switch to baidu
# Todo: write file to /tmp
def get_ping_niohouse():
    ip_list = [
        "10.33.13.1",   # 东方广场
        "10.33.9.1",    # 理想国际
        "10.33.17.1",   # 广州IFC
        "10.33.77.1",   # 上海中心
        "10.33.1.1",    # 太古汇
        "10.33.57.1",   # 上海万象城
        "10.33.65.1"    # 深圳
    ]
    username = ""
    password = ""
    flag = 0
    for ip in ip_list:
        res = ssh_cisco_to_run_ping(ip, username, password, "www.baidu.com")
        if res:
            os.system("echo 1 > /tmp/baidu_ping_" + ip)
            os.system("echo " + str(res) + " > " + "/tmp/baidu_res_" + ip)
        else:
            os.system("echo 0 > /tmp/baidu_ping_" + ip)
        flag += 1

    return flag

# test network quality: switch to 云信
def get_ping_niohouse_yunxing():
    ip_list = [
        "10.33.13.1",   # 东方广场
        "10.33.9.1",    # 理想国际
        "10.33.17.1",   # 广州IFC
        "10.33.77.1",   # 上海中心
        "10.33.1.1",    # 太古汇
        "10.33.57.1",   # 上海万象城
        "10.33.65.1"    # 深圳
    ]
    username = ""
    password = ""
    flag = 0
    for ip in ip_list:
        res = ssh_cisco_to_run_ping(ip, username, password, "59.111.232.172")
        if res:
            os.system("echo 1 > /tmp/yunxing_ping_" + ip)
            os.system("echo " + str(res) + " > " + "/tmp/yunxing_res_" + ip)
        else:
            os.system("echo 0 > /tmp/yuxing_ping_" + ip)
        flag += 1
    
    return flag


def putout():
    print (x)

def main():
    sched = BlockingScheduler()
    sched.add_job(get_ping_niohouse, 'interval', seconds=60)
    sched.add_job(get_ping_niohouse_yunxing, 'interval', seconds=60)
    #sched.add_job(get_ping_cdc, 'interval', seconds=5) 
    #sched.add_job(get_ping_popup, 'interval', seconds=5) 
    #sched.add_job(putout, 'interval', seconds=3) 
    #sched.add_job(available_report_daily, 'cron', day_of_week='0-6', hour=9, minute=40, end_date='2046-05-01')
    sched.start()

if __name__ == "__main__": 
    main()
