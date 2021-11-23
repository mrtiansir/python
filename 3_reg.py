#!/usr/bin/python3
# _*_ coding=utf-8 _*_


import os
import re
ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
#正则表达式查找ip，掩码，广播和mac地址
ipv4_add = re.findall('\d+\.\d+\.\d+\.\d+', ifconfig_result)[0]
netmask = re.findall('netmask\s+(\d+\.\d+\.\d+\.\d+)', ifconfig_result)[0]
broadcast = re.findall('broadcast\s+(\d+\.\d+\.\d+\.\d+)', ifconfig_result)[0]
mac_addr = re.findall('ether\s+([0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+:[0-9a-f]+)', ifconfig_result)[0]

#格式化字符串
format_string = '{:<10s} :{:<20s}'

#打印结果
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

#产生网关的IP地址
ipv4_gw_section1 = list(ipv4_add.split('.'))[:-1]
ipv4_gw = '.'.join(ipv4_gw_section1) + '.254'

#打印网关的IP地址
print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为:' + ipv4_gw + '\n')

#ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall('(0% packet loss)', ping_result)

if re_ping_result:
    print('网关可达！ ')
else:
    print('网关不可达！ ')