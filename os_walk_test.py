#!/usr/bin/python3
# _*_ coding=utf-8 _*_
import os

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


#os.walk逐层遍历指定目录树中的文件和子目录，直至最后一层，返回一个三元组（root,dirs,files)
#例如下面的例如中返回结果如下：
#------------第一次遍历--------------
# test                     ##三元组中root的内容
# ====================
# ['qytang4', 'qytang5']   ##三元组中dirs的内容
# ====================
# ['qytang1', 'qytang2', 'qytang3']    ##三元组中files的内容
# ====================
#-------------第二次遍历----------------
# test/qytang4
# ====================
# []
# ====================
# []
# ====================
#-------------第三次遍历-----------------
# test/qytang5
# ====================
# []
# ====================
# []
# ====================
#topdown
os.chdir('..')
for root, dirs, files in os.walk('test', topdown=False):
    print(root)
    print('='*20)
    print(dirs)
    print('=' * 20)
    print(files)
    print('=' * 20)


#清理文件
os.chdir('/root/remote')
for root, dirs, files in os.walk('test', topdown=False):
    for file_name in files:
        os.remove(os.path.join(root, file_name))
    for dir_name in dirs:
        os.rmdir(os.path.join(root, dir_name))
os.removedirs('test')


if __name__ == '__main__':
    pass
    