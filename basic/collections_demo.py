#namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p,tuple))

#deque
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('1')
print(q)

#defaultdict
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])#由于key2不存在，所以打印出'N/A'

#OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11), ('l', 12)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10), ('k', 11), ('l', 12)])
print(od)

#Counter Counter是一个简单的计数器，例如，统计字符出现的个数:
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)