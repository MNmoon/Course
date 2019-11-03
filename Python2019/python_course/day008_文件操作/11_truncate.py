#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''
f = open('a/oh-my-god.txt',mode='r+')

# f.seek(9)
# f.truncate() #删除光标后的值
# f.flush()
# f.close()

f.seek(9)
print(f.read())
f.truncate(12) #从开头截取到当前位置，从开头开始截取12个字节
f.flush()
f.close()