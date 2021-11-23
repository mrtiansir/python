#!/usr/bin/python3
# _*_ coding=utf-8 _*_
import re
import ipaddress

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
print(sorted(port_list, key=lambda x: (int(re.match('^eth\s1/101/(\d+)/(\d+)', x).groups()[0]), int(re.match('^eth\s1/101/(\d+)/(\d+)', x).groups()[1]))))

# list = [c*4 for c in 'python']
# print(list)

ip_list = ['172.16.1.1', '10.1.2.1', '192.168.8.1', '192.168.100.5', '10.3.1.1', '172.31.1.10']

print(sorted(ip_list, key=lambda ip:ipaddress.ip_address(ip)))
#ipaddress.ip_address(ip)作用是根据字符串产生IP地址，sorted支持对IP地址进行排序



list1 = [1,2,3,4,5,6]
list2 = ['up','down','up','up','down','down']
list3 = ['eth0','eth1','eth2','eth3','eth4','eth5']

d1 = dict(zip(list2, list1))
print(d1)
d2 = dict(zip(list3, d1.items()))
print(d2)

d3 = {x.upper():x*4 for x in ['cisco', 'python', 'ccie']}
print(d3)
print(d3.get('CISCO'))

l5 = [x.upper() for x in ['cisco', 'python', 'ccie']]
print(l5)
