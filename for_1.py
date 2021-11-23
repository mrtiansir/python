#!/usr/bin/python3
# _*_ coding=utf-8 _*_


List1 = ['aaa', 111, (4,5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4,5)]

for x in List1:
    if x in List2:
        print(f'{x} in List1 and List2')
    else:
        print(f'{x} only in List1')


