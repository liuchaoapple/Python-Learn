import urllib.request
'''
request 请求模块
error 异常处理模块
parse html解析模块
robotparser robots.txt解析模块
'''

'''

#hello urllib
from urllib import request
response = request.urlopen('https://www.zhihu.com/question/286512966/answer/450313380')
print(response.read().decode('utf-8'))

#post
from urllib import parse
from urllib import request
data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
response = request.urlopen('http://httpbin.org/post',data=data)
print(response.read())

#timeout
import socket
from urllib import request
from urllib import error
try:
    response = request.urlopen('http://httpbin.org/get',timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
        pass
        


#响应
##响应类型
from urllib import request
response = request.urlopen('http://httpbin.org')
print(type(response))

##响应状态码、响应头
from urllib import request
response = request.urlopen('http://httpbin.org')
print(response.status)
print(response.getheaders())
print(response.getheader('server'))


#Request
from urllib import request
req = request.Request('https://python.org')
res = request.urlopen(req)
print(res.read().decode('utf-8'))
'''

'''
from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {
    'Host': 'httpbin.org',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
res = request.urlopen(req);
print(res.read().decode('utf-8'))
'''

'''
#add_header
from urllib import request,parse
url = 'http://httpbin.org/post'
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,method='POST')
req.add_header('Host','httpbin.org')
req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',)
res = request.urlopen(req);
print(res.read().decode('utf-8'))
'''

#Handler
##代理
'''
from urllib import request
proxy_handler = request.ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743',
})
opener = request.build_opener(proxy_handler)
res = opener.open('http://www.baidu.com')
print(res.read())
'''

##Cookie
'''
from http import cookiejar
from urllib import request
cookie = cookiejar.CookieJar()
handler =request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
res = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + ' = ' + item.value)
'''

###MozillaCookieJar
'''
from http import cookiejar
from urllib import request
filename = 'cookie_baidu.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler =request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
res = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + ' = ' + item.value)
cookie.save(ignore_discard=True,ignore_expires=True)
'''

###LWPCookieJar
'''
from http import cookiejar
from urllib import request
filename = 'cookie_baidu.txt'
cookie = cookiejar.LWPCookieJar(filename)
handler =request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
res = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + ' = ' + item.value)
cookie.save(ignore_discard=True,ignore_expires=True)
'''

###读取cookie
from http import cookiejar
from urllib import request
filename = 'cookie_baidu.txt'
cookie = cookiejar.LWPCookieJar(filename)
cookie.load(filename=filename,ignore_discard=True,ignore_expires=True)
handler =request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
res = opener.open('http://www.baidu.com')
print(res.read().decode('utf-8'))

#异常处理模块urllib.error
