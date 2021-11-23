#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import re

# print(re.search('www', 'runoob.www.com').span())
# print(re.search('com', 'www.runoob.com'))

phone = "2004-959-559 # 这是一个国外电话号码"

num = re.sub('#.*', "", phone)
print('电话号码是：' + num)

num = re.sub('\D', "", num)
print('电话号码是：' + num)

if __name__ == '__main__':
    pass
    