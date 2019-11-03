#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@Author Chunyan Guo

'''

f = open('a/dishes.txt',mode='r+')

#r+先读后写
print(f.read(1)) #读取1个字节

f.write("胡辣汤") #r+模式，执行了读操作，那么写操作都在文件的末尾，和光标没有关系


for line in f:
    print(line)


# f.write("ab")  #一开始就先写再读，在文件的开头写入，写入的是字节，那么会把原来的内容覆盖
#r+模式  正确的做法:先读后写