import os

rpid = os.fork()
rpid = os.fork()
rpid = os.fork()
rpid = os.fork()
x = 0
if rpid < 0:
    print("fork调⽤失败。 ")
elif rpid == 0:
    print("我是⼦进程（ %s） ， 我的⽗进程是（%s） " % (os.getpid(), os.getppid()))
    x += 1
else:
    print("我是⽗进程（ %s） ， 我的⼦进程是（ %s） " % (os.getpid(), rpid))

print("⽗⼦进程都可以执⾏这⾥的代码")
