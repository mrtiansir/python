#!/usr/bin/python3
# _*_ coding=utf-8 _*_


import os
import time
import re

while True:
    time.sleep(1)
    print('等待1秒重新开始监控')
    netstat_result = os.popen('netstat -nlupt').read()
    if re.findall('\d+\.\d+\.\d+\.\d+:80\s+', netstat_result):
        print('HTTP (TCP/80) 服务已经被打开')
        break






