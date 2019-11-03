#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

#返回传入列表或元组对象的所谓奇数位索引对应的元素，并返回
# def func(lst):
#     return lst[1::2]
#
# def func1(lst):
#     result = []
#     for i in range(len(lst)):
#         if i % 2 ==1:
#             result.append(lst[i])


#判断用户输入对象(字符串 列表 元组) 长度是否大于5

# def func2(obj):
#     # if len(obj) >5 :
#     #     return  True
#     # else:
#     #     return False
#     return len(obj) > 5  #直接返回，比上面简单


#检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者

# def func3(lst):
#     if len(lst) > 2:
#         return lst[:2]
#

#计算传入函数的字符串中，数字，字母 空格 以及其他内容的个数，并返回结果 isalpha()--

# def func4(s):
#     zimu = 0
#     shuzi = 0
#     kongge = 0
#     other = 0
#     for c in s:
#         if c.isalpha(): #判断是否字母
#             zimu += 1
#         elif c.isdigit(): #判断数字
#             shuzi += 1
#         elif c.isspace(): #判断空格
#             kongge += 1
#         else:
#             other += 1
#     return zimu,shuzi,kongge,other
# print(func4("acdb1234 $$$$ "))


#接受2个数字，返回比较大的那个
# def func5(a,b):
#     # if a >b :
#     #     return a
#     # else:
#     #     return b
#     return a if a > b else b #三目运算，计算中间的为真返回前面的，否则返回后面的，用于简单的比较

#检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# def func7(di):
#     for key,value in di.items():
#         if len(value) > 2:
#             di[key] = value[:2]
#     return di
# d = {'k1':'fgdc','k2':[1,2,3,4]}
# print(func7(d))
#


#函数只接受1个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，字典的键值对为此列表的索引及对应的元素
lst = [11,22,33]
#返回字典 d = {0:11,1:22,2:33}

# def func8(lst):
#     if type(lst) != list:     #判断传入参数是列表，用排除法判断
#         print('扔出一个异常')
#
#     d = {}
#     for i in range(len(lst)):
#     d[i] = lst[i]
#     return d
# print(func8(lst))

#接收 姓名 性别 年龄 学历，用户输入信息后，将内容传到函数中，函数接受内容追加到一个student_msg文件中

#创建一个student_msg的文件

# def func9(name,sex,age,edu):
#     with open('student_msg.txt',mode='a') as f:
#         f.write(name + "_" + sex + "_" + str(age) + "_" + edu)
#
# #func9('suiyue','female','26','大学本科')
#
#
#
# #输入学生信息name,gender,age,edu，gender默认值为男，输入Q或q则退出
# while 1:
#     tishi = '输入学生信息，输入Q或q则退出:'
#     if tishi.upper() == "Q" or tishi.lower() == "q":
#         break
#     name = input("请输入姓名:")
#     age = input("请输入年龄:")
#     edu = input("请输入学历:")
#     sex = input("请输入性别:")
#     #gender = '男' if gender = '' else '女'  #比函数中使用默认值好用
#     func9(name,sex,age,edu)
#

#写一个函数用于注册，另一个函数用于登录*********************
# def register(name,pwd):
#     with open('user_info.txt',mode='r+') as f:  #r+先读后写，光标始终在末尾
#         for line in f:
#             if line == "": #防止空行*********
#                 continue
#             if line.split('_')[0] == name:
#                 print("用户名已存在")
#                 return False
#         else: #写入文件中注册
#             f.write(name + "_" + str(pwd) + "\n") #记得加上换行符**********
#     return True  #前面后返回False,这里是正常的流程结束要返回True*********
#
# name,pwd = input("请输入用户名:"),input("请输入密码:")
# register(name,pwd)

def login(name,pwd):
    with open('user_info.txt',mode='r') as f:
        for line in f:
            if line.strip() == name + "_" + str(pwd):  #防止空行**********
                return True
        else:
            return False
# name,pwd = input("请输入用户名:"),input("请输入密码:")
# login(name,pwd)

#3次登录机会

for i in range(2,-1,-1):
    ret = login(input('input user name:'),input('input pwd:'))
    if ret:
        print('login success')
        break
    else:
        print('user name or pwd input error,you can try %s times' % i)

































