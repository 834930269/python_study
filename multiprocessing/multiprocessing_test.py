'''Windows没有fork
print('process (%s) start...' % os.getpid())
#only works on Unix/Linux/Mc:
pid=os.fork()
if pid==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''
from multiprocessing import Process
import os

# 子进程要执行的代码,必须用命令行才会显示
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
