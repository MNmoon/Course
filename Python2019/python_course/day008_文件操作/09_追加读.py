#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''


f = open('dishes.txt',mode='a+')
f.write("饺子") #a+，只要是写，光标都在末尾

f.seek(0,0)  #光标移动到开始，后面才能读取到内容
print(f.read())

