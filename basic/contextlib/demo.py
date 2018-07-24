from contextlib import contextmanager
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

#closing
#如果一个对象没有实现上下文，我们就不能把它用于with语句。
# 这个时候，可以用closing()来把该对象变为上下文对象。
#closing是一个经过@contextmanager装饰的generator
## 例如，用with语句使用urlopen()：

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
'''
closing是一个经过@contextmanager装饰的generator

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close() 

'''