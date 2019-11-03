#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

# def fun1():
#     print("我是func1")
#
# def fun2():
#     print("我是func2")
#
# def fun3():
#     print("我是func3")
#
#
# def fun1():
#     print("我是func1")
#
#
# def fun2():
#     print("我是func2")
#     fun1()
#
#
# def fun3():
#     fun2()
#     print("我是func3")
#
# fun3()
#
# #上面这样的不是嵌套，只是互相调用


# def outer():
#     def inner(): #内部作用域，外部不能访问
#         print('我在内部')
#     print('我在外部')
#     inner()
# outer()
# #顺序: 定义外部函数  调用外部函数 定义内部函数 打印外部函数 调用内部函数
#
# outer()  #只打印外部,
# #inner()  #不能访问内部

# def outer():
#     print("我是外面的")
#     def inner1():
#         print('我是里面的1')
#     inner1()
#     def inner2():
#         print('我是里面的2')
#     print("我是外面的收尾")
# outer()


# def outer():
#     print("我是外面的")
#     def inner1():
#         def inner2():
#             print('我是里面的2')
#         inner2()
#         print('我是里面的1')
#     inner1()
#     print("我是外面的收尾")
#
# outer()


# a  = 10
#
# def fun():
#     a = 20
#     print(a)
#
# print(a) #10
# fun() #20
# print(a)#10


# a  = 10
#
# def fun():
#     a += 20  #报错，全局中的变量在这里不能修改
#     print(a)
#
# print(a) #10
# fun() #20
# print(a)#10

# a  = 10
#
# def fun():
#     global a  #当前作用域中的说那个的a是全局中的变量
#     a = 20 #修改的是全局中的变量a=20
#     print(a)
#
# print(a) #10
# fun() #20
# print(a)#20


# def outer():
#     a = 10
#     def inner():
#         a = 20
#         print(a)
#     print(a)
#     inner()
#     print(a)
#
# outer()

# def outer():
#     a = 10
#     def inner():
#         nonlocal  a #找的是局部中距离他最近的变量
#         a = 20 #改变距离他最近的变量的值，重新赋值
#         print(a)
#     print(a)
#     inner()
#     print(a)
#
# outer()

# #
# a = 10
# def fun():
#     a = 2
#     def fun_2():
#         nonlocal a  #？？？？
#         a = 3
#         def fun_3():
#             a = 4
#             print(4)
#         print(a)
#         fun_3()
#         print(a)
#     print(a)
#     fun_2()
#     print(a)
#
# print(a)
# fun()
# print(a)


#global 引入全局变量 可以定义全局变量
#nonlocal 引入局部中距离他最近的外层变量

def fun():
    global a #没有的话  这里就自己创建一个全局变量
    a = 20



















