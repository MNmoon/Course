#!/usr/bin/python
# -*- coding: UTF-8 -*-

result = []

with open('a/2019-10-23.log',mode='r') as f:
    #日志第一行显示title:时间|名字|动作
    hang = f.readline() #读取一行
    title = hang.split("|")
    for line in f:
        line = line.strip()
        lst = line.split('|')
        #dic = {"time":lst[0],"name":lst[1],"action":lst[2]}
        dic = {title[0]: lst[0], title[1]: lst[1], title[2]: lst[2]}
        result.append(dic)
print(result)