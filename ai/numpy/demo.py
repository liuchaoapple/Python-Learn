import numpy as np
#numpy基础
'''

'''
#shape管理

#Copies and Views

#高级
##Broadcasting rules
'''
    numpy.broadcast
    broadcast包定义了numpy如何处理不同维度的矩阵
'''
a = np.array([1.0,2.0,3.0])
print([2,2,2]*a)
#索引
##
##
##
##

#线性代数Linear Algebra
##简单的数组操作

#其他
##Automatic Reshaping
a = np.arange(30)
a.shape = 2,-1,3    #-1 means "whatever is needed"
'''
    2,-1,3 等价 2,5,3
    只要能拆成n个数相乘等于30即可
'''
a.shape = 1,6,5
# print(a.shape)
# print(a)

##Vector Stacking
x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
y = np.arange(5)                          # y=([0,1,2,3,4])
print(np.r_[1:14,0,4])
'''
    垂直方向叠加
'''
m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
                                          #     [0,1,2,3,4]])
'''
    水平方向叠加
'''
xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])


##Histograms直方图
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# 给定均值和方差，随机初始化矩阵
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=1,color='red')       # matplotlib version (plot)
plt.show()

#numpy版直方图
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()