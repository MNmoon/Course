#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''


#总结  函数名可做列表元素  返回值(return inner) 和 参数

# #函数名作为返回值
# def outer():
#     def inner():
#         print('i am inner')
#     return inner
# # outter() #返回inner
# # outer()() #相当于inner()
#
# ret = outer()
# ret()
#
#

# a = ""
# b = ""
# c = ""
# c = ""
# lst = [a,b,c,d]
# for el in lst:
#     print(el)

# #函数名作为lst元素
# def chi():
#     print('吃')
# def he():
#     print('喝')
# def du():
#     print('赌')
# def chou():
#     print('抽')
#
# lst = [chi,he,du,chou]  #函数也可以当参数传递
# for el in lst:
#     el()  #相当于chi() he() du() chou()

#
# #错误示范
# def a():
#     pass
#
# print(a+10)  #函数名是变量，淡水不允许执行加法 ，TypeError: unsupported operand type(s) for +: 'function' and 'int'
#
#
#
# #函数名作为参数
# def fun(abc):
#     abc()  #传入函数  相当于调用函数fun2() 打印 i am fun2
#     print(abc) #打印函数的内存地址
# def fun2():
#     print('i am fun2')
# fun(fun2)


# #多态
# def daguanren():
#     print('我是盼盼，我喜欢度涨幅')
#
# def panpan():
#     print('我是xx，我喜欢xxxx')
#
# def xiaohuahua():
#     print('我是小花花，我喜欢xxxx')
#
#
# def wangpo(nv,nan):  #核心业务逻辑 ，替换了其他的函数即可，通用
#     nv()
#     nan()
#
# wangpo(daguanren,panpan)  #王婆代理了大官人和盼盼 多态


#
# #函数名经过多次传值  容易找不到具体是哪个函数  xx.__name__ -->查看调用的是哪个函数
#
# def chi():
#     print('我是吃')
#
# ha = chi
# he = ha
# dingding = he
# dingding()  #chi()
# print(dingding())  #dingding()相当于chi()  函数本身没有返回 则接收值为None
# print(dingding)   #多次传递
# print(dingding.__name__)   #打印


def play(wanju1,wanju2,wanju3):
    """
        这是一个关于玩的函数
    :param wanju1:玩具1
    :param wanju2:玩具2
    :param wanju3:玩具3
    :return:开心
    """

    print("我在玩荡秋千")
    return "开心"
play('独木桥','独轮车','足球')
print(play.__doc__) #查看函数的说明  document

print(str.join.__doc__)  #查看字符串join的方法说明








