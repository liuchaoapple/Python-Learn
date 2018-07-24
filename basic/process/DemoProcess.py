from multiprocessing import Process
import os


# ⼦进程要执⾏的代码
def run_proc(name):
    print('⼦进程运⾏中， name= %s ,pid=%d...' % (name, os.getpid()))

if __name__ == '__main__':
    print('⽗进程 %d.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('⼦进程将要执⾏')
    p.start()
    p.join()
    print('⼦进程已结束')