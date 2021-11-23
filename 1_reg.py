#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

result = re.match('^(\d+)\s+(\w+\.\w+\.\w+)\s+([A-Z]+)\s+(\w+\d+/\d+/\d+)$', str).groups()
print(f'{"VLAN ID":<10s} : {result[0]:<20s}')
print(f'{"MAC":<10s} : {result[1]:<20s}')
print(f'{"Type":<10s} : {result[2]:<20s}')
print(f'{"Interface":<10s} : {result[3]:<20s}')

    