import numpy as np
from numpy import pi
import matplotlib.pyplot as plt



a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)   #数组中每个元素的字节大小
print(a.size)   #元素个数
print(type(a))

b = np.array([6, 7, 8])
print(type(b))

a = np.array([2,3,4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)
a = np.array([1,2,3,4])
print(a)
b = np.array([(1.5,2,3), (4,5,6)])
print(b)
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)

print(np.zeros( (3,4) ))
print(np.ones( (2,3,4), dtype=np.int16 ))
print(np.empty((2,3)))

print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))

print(np.linspace( 0, 2, 9 ))
x = np.linspace( 0, 2*pi, 100 )
print(x)
f = np.sin(x)
print(f)


print('histogram柱状图')
mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
plt.hist(v, bins=50, normed=1)
plt.show()

(n, bins) = np.histogram(v, bins=50, normed=True)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()
