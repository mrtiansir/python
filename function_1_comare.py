#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import copy

def compare(list1, list2):
    same_list = [x for x in list1 if x in list2]
    diff_list = copy.deepcopy(list1)
    for y in same_list:
        print(f'{y} in List1 and List2')
        diff_list.remove(y)
    for z in diff_list:
        print(f'{z} only in List1')


if __name__ == '__main__':
    list1 = ['aaa', 111, (4,5), 2.01]
    list2 = ['bbb', 333, 111, 3.14, (4,5)]
    compare(list1, list2)
