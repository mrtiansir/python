#!/usr/bin/python3
# _*_ coding=utf-8 _*_

#将传入函数的多个参数，以元组形式赋值给变量args
def l(x,y,z):
    print(x,y,z)

#将传入函数的多组映射参数，以字典形式赋值给变量args
def t(username,password,host):
    print(username,password,host)

#将传入函数的参数分段，赋值给x，以元组形式赋值给变量pargs，以字典形式赋值给kargs
def w(x,*pargs,**kargs):
    print(x,pargs,kargs)




if __name__ == '__main__':
    list = [1,2,3]
    l(*list)
    dict = {'username':'admin', 'password':'Cisc0123', 'host':'192.168.5.131'}
    t(**dict)

    