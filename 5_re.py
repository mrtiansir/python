#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import re

str1 = 'Port-channel1.189   192.168.189.254  YES    CONFIG  up'

result = re.match('^(\S+\d+\.?\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(\w+)$', str1).groups()

print('-'*80)
print(f'{"接口":<10s} : {result[0]:<20s}')
print(f'{"IP地址":<10s} : {result[1]:<20s}')
print(f'{"状态":<10s} : {result[2]:<20s}')

