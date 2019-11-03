#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@File :05_迭代器.py.py
@Time : 2019/11/2 9:18 PM
@Author : Chunyan Guo
@Version : 1.0
@Contact : xxx@qq.com
@Desc :None
'''


# for c in 123:
#     print(c)  #error  字符串不可迭代

#可迭代iterable: 字符串  lst  tuple dict set open() range()

#dir() 可以查看数据类型中可以执行的方法


# s = "alex"
# print(dir(s)) #查看s可进行的操作 在字符串中发现了 __iter__. 没有__next__

# a = 123
# print(dir(a))  #无__iter__

lst = [1,2,3]
#print(dir(lst)) #__iter__ 有它 可迭代

it = lst.__iter__() #iterator迭代器

#print(it.__next__())     #python3.6中
# print(it.next())
# print(it.next())
# print(it.next())
#
# print(it.next()) #？？？   StopIteration

#对于异常的处理
while 1:
    try:
        print(it.next())
    except StopIteration:
        print("game over")
        break
#for循环的原理
for el in lst:
    print(el)
else:
    print("结束了")




