#1.入门
##1.1   创建scrapy工程
    scrapy startproject tutorial
        在当前目录下创建scrapy工程,命名为tutorial
        tutorial/
            scrapy.cfg            # deploy configuration file
            tutorial/             # project's Python module, you'll import your code from here
                __init__.py
                items.py          # project items definition file
                middlewares.py    # project middlewares file
                pipelines.py      # project pipelines file
                settings.py       # project settings file
                spiders/          # a directory where you'll later put your spiders
                    __init__.py
##1.2   在工程下文件夹spiders下创建quotes_spider.py文件
##1.3   运行scrapy crawl quotes
    命令执行完成后,在工程根目录下生成quotes-1.html和quotes-2.html文件。