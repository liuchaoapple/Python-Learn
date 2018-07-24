import pandas as pd
import numpy as np
#创建一个空的Series
s = pd.Series()
print(s)
print('--'*40)
#从ndarray创建一个Series
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print('--'*40)
#指定index
s = pd.Series(data,index=[100,101,102,103])
print(s)
print('--'*40)
#从字典创建一个Series
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
print('--'*40)
#指定index
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print('--'*40)
#从标量创建一个Series,如果数据是标量值，则必须提供索引
s = pd.Series(5, index=[1,2,3,4,5,6,7])
print(s)
print('--'*40)

#从具有位置的Series中访问数据
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
##检索第一个元素
print(s[0])
print('--'*40)
##检索系列中的前三个元素
print(s[:3])
print('--'*40)
##检索最后三个元素
print(s[-3:])
print('--'*40)

#使用标签检索数据(索引)
##使用索引标签值检索单个元素
print(s['a'])
print('--'*40)
##使用索引标签值列表检索多个元素
print(s[['a','c','d']])
print('--'*40)

