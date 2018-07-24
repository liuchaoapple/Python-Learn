'''
    Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
'''

import itertools
#"无限迭代器"
'''
#count()方法
natuals = itertools.count(1)
for n in natuals:
    print(n)
'''

'''
#cycle()方法
cs = itertools.cycle('ABC')
for c in cs:
    print(c)
'''

'''
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('ABC',100)
for n in ns:
    print(n)
'''

'''
#无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来
# 事实上也不可能在内存中创建无限多个元素。
#无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
#takewhile
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<30,natuals)
print(list(ns))
'''

'''
#chain()
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
#chain()可有多个参数
for c in itertools.chain('ABC','123','XYZ'):
    print(c)
'''

'''
#groupby()
#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBBCCCADAA'):
    print(key,list(group))
'''

'''
#groupby()忽略大小写
for key,group in itertools.groupby('AAABBBCccADaa',lambda c:c.upper()):
    print(key,list(group))
'''

#practise
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

#注意:itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。