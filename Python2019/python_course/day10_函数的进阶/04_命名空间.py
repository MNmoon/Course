#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''
#
# #内置命名空间，python自己开辟的空间
# print()
#
# #全局命名空间
#
# a = 10  #全局作用域
# print(a)
#
# #局部命名空间
# def func():
#     a = 10  #局部作用域
#     print(a)

#命令空间顺序 内置命名空间 - 全局命名空间 -- 局部命名空间

#取值顺序 局部  全局  内置

#作用域:变量或者函数的声明周期
#全局作用域：全局名称空间 + 内置名称空间
#局部作用域：局部命名空间
#1.globals() 查看全局作用域中所有内容
qiao = "乔峰"
def kang():
    bgm = 'ggggg'
    print('娃哈哈')
    print(locals())
kang()
#print(globals()) #查看全局作用域中内容 globals() and locals()是内置函数
#print(locals()) #查看当前作用域中内容
