#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

#写函数，接受N个数字并计算其和
#
# def fun(*n):
#     sum = 0
#     for el in n :
#         sum += el
#     return sum
# print(fun(1,2,3,4,5))

# #读程序，写出a b c的值
# a = 10
# b = 20
# def test(a,b):
#     print(a,b)
# c =test(a,b) #没有返回，None
# print(c)

#读程序，写出a b c的值
# a = 10
# b = 20
# def test(a,b):
#     a = 3
#     b = 5
#     print(a,b) #3，5
# c =test(a,b) #没有返回，None
# print(c)
# print(a,b)



#传入字符串  元组 列表等
# def fun(*args): #str list tuple
#     print(args)
#
# fun("haha",[1,2,3],(2,3,4))
#
#
# def fun(*args): #str list tuple
#     list = []
#     for el in args: #el传进来的就是可迭代的对象，需要在循环一次
#         for e in el:
#             list.append(e)
#     tu = tuple(list)
#     print(tu)
#
#
# fun("haha",[1,2,3],(2,3,4))
#
#

# #传入函数中的多个实参均为字典，将每个实参的键值对，依次添加到动态参数kwargs中
# #最终结果为'a': 1, 'b': 2}
# def fun(**kwargs):
#     print(kwargs)
#
# fun(**{"a":1,"b":2})
#检查错误
# def fun():
#     a = 1
#     def inner():
#         a += 1  #error
#         print(a)
#     inner()
# fun()

#传入参数，将参数用下划线拼接[1,'old','new']  --- 1_old_new
# def fun(it):
#     # result = ""
#     # for el in it:
#     #     result += str(el) + "_"
#     # #return "_".join(it)
#     # return result[:-1]
#
#     for i in range(len(it)):
#         el = str(it[i])
#         it[i] = el
#     return "_".join(it)


# def fun(it):
#     return "_".join(it)
# #fun([1,'alex','haha']) #对于数字的  不能用join-str

#返回传入参数的最大最小值，以字典的形式 --max内置函数
# def fun(*n):
#     retutn {"max":max(n),"min":max(n)}  #？？？？
# print(fun(1,2,3,4,5,6))
#


# #求阶乘
# def fun(n):
#     sum = 1
#     for i in range(n,0,-1)
#         sum *= i
#     return sum
# print(fun(n))

#返回一个扑克牌列表 里面有52项 每一项是一个元组
#例如 [('红心'，2)]

#花色  红色芳草
#点数 A234567890JQK
#两大阵营 两两组合 --->笛卡尔积
#13*4

# hua = ["红心","黑桃","梅花","方块"]
# dian = ['A',2,3,4,5,6,7,8,9,10,'J','Q','k']
#
# def fun():
#     result = []
#     for h in hua:
#         for d in dian:
#             result.append((h,d))
#     return result
# print(result)
#
#
# def wrapper():
#     def inner():
#         print(1)
#     return inner #函数名可以作为变量返回
#
# fn = wrapper()
# fn()

#完成99乘法---阶乘
#1*1
#2*1 2*2
#3*1 3*2 3*3
#.......
#9*1 9*2 ...9*9

# for i in range(1,10):
#     for j in range(1,i+1): #核心
#     print("%s*%s=%s" % (i,j,i*j),end=" ") #???

#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *


def fun():
    print('a')

print(fun)  #打印的是函数的内存地址





