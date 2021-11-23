#!/usr/bin/python3
# _*_ coding=utf-8 _*_


import os
import re

route_n_result = os.popen("route -n").read()

gw = re.findall('(\d+\.\d+\.\d+\.\d+)\s+\d+\.\d+\.\d+\.\d+\s+UG', route_n_result)[0]

print("网关为:" + gw)
    