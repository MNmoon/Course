#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

# f = open('dishes.txt',mode='a+')
# print(f.tell())  #打印光标在末尾


# f = open('dishes.txt',mode='a+')
#
# #a+光标始终在末尾，需要先移动到开始位置才能读取到内容
# f.seek(0,0)
# print(f.read(1))  #读取的字符
#
# f.seek(0,0)  #移动到开头
# print(f.tell())  #打印光标,显示的字节
# f.write('我的儿子')
#
# #先将光标移动到开头，再读内容
# f.seek(0,0)  #移动到开头
# print(f.read())  #读取所有内容

#得写的时候 以字符为单位；光标移动单位是字节
#光标移动 0开头 1当前位置  2末尾
# seek(0,2)
# seek(偏移量，位置)




f = open('dishes.txt',mode='w+')

# f.write('vvvvvvv')  #只要写，就会把内容覆盖
# f.seek(0,0)
# print(f.read())  #w+只有先写，然后将光标移动到开头，才能读取内容

print(f.read())  #W+模式一开始无法直接读取


#w+正确使用方式:w+只有先写，然后将光标移动到开头，才能读取内容





