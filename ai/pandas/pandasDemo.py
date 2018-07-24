import numpy as np
import pandas as pd

#对象创建
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print("--"*40)
#通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
dates = pd.date_range('20170101', periods=7)
print(dates)
print("--"*40)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print(df)
print("--"*40)
#通过传递可以转换为类似系列的对象的字典来创建DataFrame
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20170102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)
print("--"*40)
#查看框架的顶部和底部的数据行
dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
#取前5(默认)个数据
print(df.head())
print("--"*40)
#取后5(默认)个数据
print(df.tail())
print("--"*40)

#显示索引，列和底层numpy数据
dates = pd.date_range('20170101', periods=7)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list('ABCD'))
print("index is :" )
print(df.index)
print("--"*40)
print("columns is :" )
print(df.columns)
print("--"*40)
print("values is :" )
print(df.values)
print("--"*40)
#描述显示数据的快速统计摘要
print(df.describe())
print("--"*40)

dates = pd.date_range('20170101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#置换操作
print(df.T)
print("--"*40)
print(df)
print("--"*40)
#通过列排序
print(df.sort_index(axis=1, ascending=False))
print("--"*40)
#按值排序
print(df.sort_values(by='B'))
print("--"*40)
#选择区块
print(df['A'])
print("--"*40)
#选择通过[]操作符，选择切片行
print(df[0:3])
print("--"*40)
#指定选择日期
print(df['20170102':'20170103'])
print("--"*40)


#按标签选择
print(df.loc[dates[0]])
print("--"*40)

#通过标签选择多列
print(df.loc[:,['A','B']])
print("--"*40)
#显示标签切片，包括两个端点
print(df.loc['20170102':'20170104',['A','B']])
print("--"*40)
#减少返回对象的尺寸(大小)
print(df.loc['20170102',['A','B']])
print("--"*40)
#获得标量值
print(df.loc[dates[0],'A'])
print("--"*40)
#快速访问标量(等同于上条命令)
print(df.at[dates[0],'A'])
print("--"*40)

#通过位置选择
#通过传递的整数的位置选择
print(df.iloc[3])
print("--"*40)
#通过整数切片
print(df.iloc[3:5,0:2])
print("--"*40)
#通过整数位置的列表
print(df.iloc[[1,2,4],[0,2]])
print("--"*40)
#明确切片行
print(df.iloc[1:3,:])
print("--"*40)
#明确切片列
print(df.iloc[:,1:3])
print("--"*40)
#明确获取值
print(df.iloc[1,1])
print("--"*40)
#快速访问标量
print(df.iat[1,1])
print("--"*40)

#布尔索引
##使用单列的值来选择数据
print(df[df.A > 0])
print("--"*40)
print(df[df.A <= 0])
print("--"*40)
##从满足布尔条件的DataFrame中选择值
print(df[df > 0])
print("--"*40)
print(df[df <= 0])
print("--"*40)

#使用isin()方法进行过滤
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print(df2)
print("============= start to filter =============== ")
print(df2[df2['E'].isin(['two','four'])])
print("--"*40)


