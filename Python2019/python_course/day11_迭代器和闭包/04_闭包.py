#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@File :04_闭包.py.py
@Time : 2019/11/2 12:04 PM
@Author : Chunyan Guo
@Version : 1.0
@Contact : xxx@qq.com
@Desc :None
'''


# def fun():
#     a = 10  #局部变量
#     print(a)
# fun()
#
# print(a)  #找值 始终从里面向外面找   外面访问不到局部变量
#
#

# a = 20
# def fun():
#     a = 10  #局部变量
#     print(a)
# fun()
#
# print(a)  #找值 始终从里面向外面找   外面访问不到局部变量  局部变量是安全的
#

#
# #全局变量可能是不安全的  可能会被函数修改 那要怎么才安全？
# a = 20
# def fun():
#     global a
#     a = 10  #修改全局变量
#     print(a)
# fun()
#
# print(a)  #找值 始终从里面向外面找   外面访问不到局部变量



#
#闭包可以保护我们的变量
#写法:在外层函数中声明一个变量，在内层函数使用或者返回这个变量
#这个结构叫闭包
#1.保护变量不会被其他的修改
#2.闭包中的变量常驻内存 (inner执行位置不确定，但inner没有执行前a不会被释放)--全局变量也会常驻内存
#
# def outer():
#     a = 10  #内部，被包裹被保护，其他函数不能改变变量值
#     def inner():
#         print("i am inner") #在内部使用的外面的变量
#         print(a)
#
#     def inner_2():
#         print(a+20) #在内部使用外部的变量
#     return inner #返回内部函数
#
# #ret  = outer() #得到的是inner -->即是inner的内存地址
# ret = outer()
# ret()
#
# #怎么看有没有闭包
# print(ret.__closure__)  #有东西就是闭包((<cell at 0x10cbd3ad0: int object at 0x7f7f19f05430>,))，没东西就是None
#
# def haha():
#     print("i don't have bibao")
# print(haha.__closure__)


#
#
# #闭包的应用,保护变量，常驻内存-->爬虫，与网络的瓶颈有关系
# from urllib import urlopen
#
# def fun():
#     content = urlopen("http://www.xiaohua.com/").read()
#     def inner():
#         return content
#     return inner
# print("加载中...")
# f = fun()  #inner
# print("加载完毕...")
# #使用常驻内存中的变量
# print(f())
# print(f())
# print(f())






















