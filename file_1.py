#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import os
import shutil

#创建测试文件夹和文件
os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')
#如果测试目录下类型为文件的对象，逐行读取，判断文件中内容是否包含"qytang"，如果包含将文件名追加至列表list1
list1 = []
for x in os.listdir(os.getcwd()):
    if os.path.isfile(x):   #如果为文件
        for line in open(x, 'r'):   #逐行迭代文件中的内容
            if 'qytang' in line:    #判断每行的内容中是否包含"qytang"
                list1.append(x)     #如果包含"qytang"，将文件名加入列表，并停止迭代查询文件中余下的行内容
                break

#打印结果
print('文件中包含"qytang"关键字的文件为:\n')
for x in list1:
    print(x)

#删除测试的文件夹和文件
os.chdir('..')   #进入当前目录的上层目录
shutil.rmtree('test')


    