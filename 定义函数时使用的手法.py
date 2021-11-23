#!/usr/bin/python3
# _*_ coding=utf-8 _*_

#将传入函数的多个参数，以元组形式赋值给变量args
def l(*args):
    print(args)

#将传入函数的多组映射参数，以字典形式赋值给变量args
def t(**args):
    print(args)

#将传入函数的参数分段，赋值给x，以元组形式赋值给变量pargs，以字典形式赋值给kargs
def w(x,*pargs,**kargs):
    print(x,pargs,kargs)



if __name__ == '__main__':
    l(1,2,3,4)
    t(a=1, b=1, c=1)
    w(1,2,3,4,5,a=1,b=2)
