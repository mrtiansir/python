#!/usr/bin/python3
# _*_ coding=utf-8 _*_


import time

while True:
    try:
        time.sleep(2)
        print('请输入ctrl + c来停止这个循环')
    except KeyboardInterrupt:
        print('接收到管理员的ctrl + c！')
        print('退出程序')
        break

    