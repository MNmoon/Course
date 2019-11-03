#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@File :02_生成器.py.py
@Time : 2019/11/2 10:18 PM
@Author : Chunyan Guo
@Version : 1.0
@Contact : xxx@qq.com
@Desc :None
'''
#生成器,本质是迭代器，写法和迭代器不一样，用法和迭代器一样
#生成器函数，函数中带有yield，执行生成器函数的时候返回生成器，而不不是执行这个函数
#
# def fun():
#     print("hello,my name is sailiya")
#     #return "希腊来的大哥"
# # fun() #f接收返回的数据  返回的数据
# # print(fun()) # 执行函数中的打印  打印返回的数据
#     #yield "希腊来的2哥"
#     yield  "the second brother"
#
# ret = fun() #接收的迭代器
# print(ret)
# s = ret.next() #当执行.next()时，函数才开始真正的执行
# print("接收的是:",s)
#
#


# def fun():
#     print("open your phone")
#     print("open your momo")
#     yield "phone"
#     print("make a date with your sister")
#     print("go out to drink")
#     yield "computer"
#
#
# gun = fun() #生成器
# ret1 = gun.next()
# print(ret1)
# ret2 = gun.next()
# print(ret2)

# #打印1000件衣服
# def fun():
#     for i in range(1000):
#         print("close %s " % i)
# fun()

# #使用生成器打印衣服
# def fun():
#     for i in range(1000):
#         yield "close %s " % i
# gen = fun()  #接收到生成器
# print(gen.next())
# print(gen.next())
# print(gen.next())
# print(gen.next())
# print(gen.next()) #找不到.next()就会报错



#总结:提升效率
#1.节省内存  几乎不占内存 一次打印一个和一次性打印1000个....
#2.惰性机制，取值一个打印一个
#3.只能向前走，每次打印都是最新的一个
#

#
#
# def fun():
#     lst = []
#     for i in range(1000):
#         lst.append("close is %s" % i)
#         if i % 50 ==0:
#             yield lst
#             lst = [] #新的装衣服的地方
# gen = fun()
# yf1 = gen.next()
# yf1 = gen.next()
# print(yf1)


#
# #send给上一个yield传值
#
# def fun():
#     print("韭菜盒子")
#     a = yield "娃哈哈"
#     print("肉包子",a)
#     b = yield "脉动"
#     print("锅包肉",b)
#     yield "冰红茶"
#
# gen = fun()
# ret = gen.send("first") #报错，不能给第一个生成器传值(他的前面没有yield)
# ret = gen.next()
# print(ret)
#
# ret = gen.send("刘伟") #给上一个yield 传值，ret此时返回值是脉动
# print(ret)

#send()和next()的区别
#send不能用在开头
#send可以给上一个yield传值，不能给最后一个yield传值


def fun():
    yield "马化腾"
    yield "李彦宏"
    yield "马云"
    yield "刘强东"
gen = fun()
# print(gen.next())
# print(gen.next())
# print(gen.next())
# print(gen.next())

#生成器的本质是迭代器
#print("__iter__" in dir(gen))  #查看是否可迭代
# for el in gen:
#     print(el)

lst = list(gen) #把生成器中每一个数据拿来组合成一个列表
print(lst)





