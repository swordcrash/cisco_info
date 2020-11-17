#!/usr/bin/env python3
# check network status on cisco 
# ping internet address on cisco switch

from netmiko import ConnectHandler
import sys 
import os


username = ''
password = ''

def ssh_cisco_to_run_ping(ip_address, username, password, URL):
    cisco = {'device_type':'cisco_ios', 'ip':ip_address,'username':username,'password':password}
    net_connect = ConnectHandler(**cisco)
    results = net_connect.send_command("ping " + URL)

    packet_available = 0
    response_avg = 0

    for result in results:
        if result == '!':
            packet_available += 1

    # get the avg from [min/avg/max = 1/4/10 ms]
    #print(results)
    print(ip_address,packet_available)
    if not packet_available:
        return 0

    lines = results.split('\n')
    for line in lines:
        tmp = line.split(' ')
        if 'Success' == tmp[0]:
            response_avg = line.split('/')[4]
            pass
    
    print(response_avg)
    return response_avg

"""         
    if packet_available:
        try:
            lines = results.split('\n')
            for line in lines:
                print(line)
            # fliter two result by ssh command
            if lines[0].split(' ')[0] != 'Translating':
                print(lines[3])
                result = lines[3].split('/')
                response_avg = result[4]
            else:
                print(lines[5])
                result = lines[5].split('/')
                response_avg = result[4]
        except: 
            pass
    else:
        print('#')

    print(response_avg)
    return response_avg
"""
def main():
    ip = sys.argv[1]
    URL = sys.argv[2]

    #URL_A = "www.baidu.com"
    #URL_B = "www.qq.com"

    if "baidu" == URL:
        AD = "www.baidu.com"
        FILE_PING_RESULT = "/tmp/baidu_ping_" + ip
        FILE_RESPONSE_TIME = "/tmp/baidu_res_" + ip
    elif "qq" == URL:
        AD = "www.qq.com"
        FILE_PING_RESULT = "/tmp/qq_ping_" + ip
        FILE_RESPONSE_TIME = "/tmp/qq_res_" + ip
        
    AVAILABLE = ssh_cisco_to_run_ping(ip, username, password, AD)
    if AVAILABLE:
        os.system("echo 1 > " + FILE_PING_RESULT)
        os.system("echo " + str(AVAILABLE) + " > " + FILE_RESPONSE_TIME)
    else:
        os.system("echo 0 > " + FILE_PING_RESULT)
        os.system("echo 0 > " + FILE_RESPONSE_TIME)
                
    os.system("chown zabbix.zabbix " + FILE_PING_RESULT)
    os.system("chown zabbix.zabbix " + FILE_RESPONSE_TIME)
            

if __name__ == "__main__":
    main()

