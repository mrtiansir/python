#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n\
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

# print(asa_conn.splitlines())  #返回一个由asa_conn中各行组成的列表

asa_dict = {}

for conn in asa_conn.split('\n'):
    re_result = re.match('\w+\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+)\s+\w+\s+(\d+\.\d+\.\d+\.\d+):(\d+),\s+\w+\s+\d+:\d+:\d+,\s+\w+\s+(\d+),\s+\w+\s+(\w+)', conn).groups()
    asa_dict[re_result[0], re_result[1], re_result[2], re_result[3]] = (re_result[4], re_result[5])

print('打印分析后的字典！\n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
format_str1 = '{:^10s}:{:^15s}|{:^10s}:{:^15s}|{:^10s}:{:^15s}|{:^10s}:{:^15s}'
format_str2 = '{:^10s}:{:^15s}|{:^10s}:{:^15s}'

print('\n格式化打印输出\n')

for key, value in asa_dict.items():
#    print(key, value)
    print(format_str1.format(src, key[0], src_ip, key[1], dst, key[2], dst_ip, key[3]))
    print(format_str2.format(bytes_name, value[0], flags, value[1]))
    print('='*105)