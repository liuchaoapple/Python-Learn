#常用库

##请求库
###urllib
    python内置请求库
    
    urllib 侧重于 url 基本的请求构造
    
    urllib2侧重于 http 协议请求的处理
    
    urllib3是服务于升级的http 1.1标准，且拥有高效 http连接池管理及 http 代理服务的功能库
    
    从 urllib 到 urllib2和 urllib3是顺应互联应用升级浪潮的，这股浪潮从通用的网络连接服务到互联网网络的头部应用：
    支持长连接的 http 访问，网络访问不断的便捷化。
####request请求模块
####error异常处理模块
####parse url解析模块
####robotparser robots.txt解析模块
    不常用

###requests
    不自动加载js，需要手工解析。

###selenium
    驱动浏览器渲染js。
    webdriver。
    不再友好支持Phantomjs。


##解析库
###re 正则表达式

###lxml

###bs4 BeautifulSoup4

###pyquery
    和jquery解析方法类似
###XPath




##存储库
###redis|redis

###mysql|pymysql

###mongo|pymongo

##其他
###django web框架
###flask web框架
###jupyter
    启动:jupyter notebook，自动打开浏览器。
    默认端口:8888
    
#爬虫基本原理
##什么是爬虫？
    请求网站并提取数据的自动化程序
##爬虫基本流程
###1.发起请求request
####request内容
    请求方式(request method):post/get/put/delete/trace/connect/header/option
    请求url
    请求头
    请求体(post)
###2.获取相应内容response
####response内容
    响应状态（状态码）
    响应头
    
###3.解析内容beautifulsoup
###4.保存数据persistence

##数据格式
    html
    json
    xml
    图片
    视频
##js渲染问题
    分析Ajax请求
    Selenium/WebDriver
    Splash
    其他库
##保存数据
    文本：txt、json、xml
    RDB：Mysql、Oracle、SQL Server
    NOSQL:Redis、MongoDB、HBase
    二进制文件
    