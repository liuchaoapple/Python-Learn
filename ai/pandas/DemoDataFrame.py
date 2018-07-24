import numpy as np
import pandas as pd
#创建一个空的DataFrame
df = pd.DataFrame()
print(df)
print('--'*40)
#从列表创建DataFrame
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print('--'*40)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print('--'*40)
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
print('--'*40)

#从ndarrays/Lists的字典来创建DataFrame
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
print('--'*40)
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)
print('--'*40)

#从列表创建数据帧DataFrame
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print('--'*40)

#通过传递字典列表和行索引来创建数据帧
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
print('--'*40)

#使用字典，行索引和列索引列表创建数据帧
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
##With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df1)
print('--'*40)
##With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df2)
print('--'*40)

#从系列的字典来创建DataFrame
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print('--'*40)

#列选择
##从数据帧(DataFrame)中选择一列。
print(df['one'])
print('--'*40)

#列添加
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
## Adding a new column to an existing DataFrame object with column label by passing new series
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print('--'*40)
print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)
print('--'*40)

#列删除
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three' : pd.Series([10,20,30], index=['a','b','c'])}
df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)
print('--'*40)
# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print(df)
print('--'*40)
# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print(df)
print('--'*40)

#行选择，添加和删除
##标签选择,可以通过将行标签传递给loc()函数来选择行
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df.loc['b'])
print('--'*40)
##按整数位置选择,可以通过将整数位置传递给iloc()函数来选择行
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df.iloc[2])
print('--'*40)
##行切片，可以使用:运算符选择多行
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print('------------------------df[2:4]------------------------')
print(df[1:3])
print('--'*40)

#附加行,使用append()函数将新行添加到DataFrame
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
print(df)
print('--'*40)

#删除行,使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。
df = df.drop(0)
print(df)
print('--'*40)