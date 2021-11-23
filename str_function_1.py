#!/usr/bin/python3
# _*_ coding=utf-8 _*_

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n \
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

list = asa_conn.splitlines()

new_list = [x.strip() for x in list]
print(new_list)



if __name__ == '__main__':
    pass
    