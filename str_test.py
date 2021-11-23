#!/usr/bin/python3
# _*_ coding=utf-8 _*_

str = '''
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-6-106015: Deny TCP (no connection) from 172.16.200.32/46636 to 119.23.80.62/8443 flags PSH ACK  on interface inside
Nov 15 2021 11:41:46: %ASA-6-106015: Deny TCP (no connection) from 172.16.200.32/46636 to 119.23.80.62/8443 flags RST ACK  on interface inside
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
Nov 15 2021 11:41:46: %ASA-3-106014: Deny inbound icmp src outside:115.238.46.50 dst inside:192.168.223.7 (type 3, code 3)
Nov 15 2021 11:41:46: %ASA-4-419002: Duplicate TCP SYN from inside:172.16.200.77/56692 to inside:192.168.32.133/7680 with different initial sequence number
'''

list1 = str.split('\n')
print(list1)
print(len(list1))

for x in list1:
    print(x)




if __name__ == '__main__':
    pass
    