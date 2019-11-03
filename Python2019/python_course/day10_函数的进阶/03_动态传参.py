#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

# #非动态传参
# def chi(a,b):
#     print(a,b)
#
# #动态传参，不定个数的参数
# def chi1(*args):
#     print("我要吃",args)
#
# chi1('rice','cookie','noodles')

#传参顺序: 位置参数  *args 默认值  **kwargs
#
# def shiyan(*args,**kwargs): #无敌的存在，什么都可以接收，python底层很多都这样
#     print(args,kwargs)
# shiyan(1,2,a='lisa',b='susan')
#
# def practice(*args):
#     print(args)
# lst = [1,2,3]
# #practice(lst[0],lst[1],lst[2])  #拆分lst然后一个个传进去
# practice(*lst)  #在实参位置  *表示打散，打散的是可迭代对象

def funct(**kwargs): # **表示把接收到的关键字参数打包(聚合)成字典
    print(kwargs) #一定是字典

d = {'a':2,'b':3,'c':4}
funct(**d) #**表示把字典打散，字典的key作为参数的名字，字典的值作为参数的值传递给形参

d2 = {1:'a','li':'wang','g':'ming'}  #坑,字典的key不能是纯数字
funct(**d2)  #

