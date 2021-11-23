#!/usr/bin/python3
# _*_ coding=utf-8 _*_

import os

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

print('文件中包含"qytang"关键字的文件为:')
print('方案一:')

for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isfile(file_or_dir):
        for line in open(file_or_dir):
            if 'qytang' in line:
                print(file_or_dir)
                break

print('方案二：')
#这是更优化的递归方案，topdown的作用：True优先遍历top目录中的内容，False优先遍历top（这里是test目录）的子目录的内容
os.chdir('/root/remote')
for root, dirs, files in os.walk('test', topdown=False):
    if files != []:
        for file_name in files:
            for line in open(os.path.join(root, file_name)):
                if 'qytang' in line:
                    print(file_name)
                    break



#完成清理工作
os.chdir('/root/remote')
for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.removedirs('test')






if __name__ == '__main__':
    pass
    