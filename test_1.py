#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import time

for i in range(1, 5):
    i += 1
    print(i)

n = int(input('pls input an integer >=0: '))
fact = 1
# for i in range(2, n+1):
#     fact = fact * i
# print(str(n) + ' factorial is ' + str(fact))
i = 2
while i <= n:
    fact = fact * i
    i += 1
print(str(n) + ' factorial is ' + str(fact))










    