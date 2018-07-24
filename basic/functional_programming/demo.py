from functools import reduce

'''
def fn(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

rst1 = reduce(fn,map(char2num,'13579'))

print(rst1)
'''


#整理成一个函数
'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))
'''

#用lambda函数进一步简化成：
'''
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('13579'))
'''

#filter
'''
import numpy as np
lst = np.arange(1,10,step=1,dtype=int)
print(lst)

lst = list(filter(lambda num:num%2 == 1,lst))

print(lst)
'''

#sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21],key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
from operator import itemgetter
L2 = sorted(L, key=itemgetter(0))
print(L2)
L2 = sorted(L, key=itemgetter(1),reverse=True)
print(L2)
L2 = sorted(L, key=lambda t:t[1],reverse=True)
print(L2)

#偏函数
import functools
int2 = functools.partial(int,base=2)
print(int2('100100101'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()