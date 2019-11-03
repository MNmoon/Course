#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''
import os

#修改文件内容
#1.修改后的内容写到副本中，然后将副本重命名
with open('a/alex.txt',mode='r') as f1,\
        open('a/alex1.txt',mode='w') as f2:
    for line in f1:
        new_line = line.replace('good','sb')
        f2.write(new_line)

time.sleep(2) #只是为看到过程采用sleep
os.remove("a/alex.txt")
time.sleep(2) #只是为看到过程采用sleep
os.rename("a/alex1.txt","a/alex.txt")

