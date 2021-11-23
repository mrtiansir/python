#!/usr/bin/python3
# _*_ coding=utf-8 _*_


import re

str = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

result = re.match('(^[A-Z]+)\s+([a-z]+)\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+([a-z]+)\s+(\d+\.\d+\.\d+\.\d+:\d+),\s+([a-z]+)\s+(\d+):(\d+):(\d+),\s+([a-z]+)\s+(\d+),\s+([a-z]+)\s+([A-Z]+)$', str).groups()

print(f'{"protocol":<15s} : {result[0]:<20s}')
print(f'{result[1]:<15s} : {result[2]:<20s}')
print(f'{result[3]:<15s} : {result[4]:<20s}')
print(f'{result[5]:<15s} : {result[6] + " 小时" + result[7] + " 分钟" + result[8] + " 秒":<20s}')
print(f'{result[9]:<15s} : {result[10]:<20s}')
print(f'{result[11]:<15s} : {result[12]:<20s}')