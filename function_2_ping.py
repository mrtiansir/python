#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        print(f'{ip} 通!')
    else:
        print(f'{ip} 不通!')



if __name__ == '__main__':
    qytang_ping('192.168.5.1')
    