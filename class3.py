import re

str1 = 'Vlan507              10.159.161.252  protocol-up/link-up/admin-up  '

result = re.match('(\w+\d)\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+(\w.*\w)/(\w.*\w)/(\w.*\w)\s*', str1).groups()

print('-'*80)
print("{0:<12s}: {1:<20s}".format('接口', result[0]))
print("{0:<12s}: {1:<20s}".format('IP地址', result[1]))
print("{0:<10s}: {1:<20s}".format('协议状态', result[2]))
print("{0:<10s}: {1:<20s}".format('物理状态', result[3]))
print("{0:<10s}: {1:<20s}".format('管理状态', result[4]))


str2 = '*  507     1418.7766.afbe   dynamic  0         F      F    Eth129/1/30'
result = re.match('\*\s+(\d+)\s+([0-9a-f]{4,}\.[0-9a-f]{4,}\.[0-9a-f]{4,})\s+(\w+)\s+(\d+)\s+(\w)\s+(\w)\s+(\w.*\d)', str2).groups()

print('-'*80)
print('{0:<15s} : {1:<20s}'.format('VLAN', result[0]))
print('{0:<15s} : {1:<20s}'.format('MAC Address', result[1]))
print('{0:<15s} : {1:<20s}'.format('Interface', result[-1]))
