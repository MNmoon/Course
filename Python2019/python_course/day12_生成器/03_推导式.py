#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
@File :03_推导式.py.py
@Time : 2019/11/3 9:01 PM
@Author : Chunyan Guo
@Version : 1.0
@Contact : xxx@qq.com
@Desc :None
'''


# #列表，装Python1 python2 python3
# lst = [] #
# for i in range(1,17):
#     lst.append('python%s' % i)
# print(lst)
#

# #列表推导式 []-->相当于创建了一个列表,[结果 for循环  if筛选]
# lst = ["python%s" % i for i in range(1,17)]
# print(lst)

#创建列表：[1，3，5，7...99]
#lst = [ i for i in range(1,100) if i % 3 == 0]  #被3整除
#lst = [ i* for i in range(1,101) if i % 3 == 0]  #被3整除的数的平方
#print(lst)

# #寻找名字中带有2个e的人
# names = [['tom','billy','jefferson','andrew','wesley','steven','joe'],['alice','jill','ana','wendy','jennifer','sherry','eva']]
# lst = [n for name in names for n in name if n.count('e') >= 2] #两层循环，这里需要返回的是n,第二层for循环的循环n
# print(lst)


#
# # #字典推导式 {key:value for 循环 if 筛选}
# #
# # dic = {"a":3,"b":2,"c":1}
# # d = {dic[k]:k for k in dic}
# # print(d)
#
# lst1 = ["东北","山东","山西"]
# lst2 = ["大拉皮","油泼面","老陈醋"]
# dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
#
# print(dic)

#集合推导式 {key for循环 if筛选}
#集合 可哈希  不重复
lst = ["周杰伦","周润达","刘德华"]
s = {el for el in lst}
print(s)