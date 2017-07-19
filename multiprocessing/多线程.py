import time,threading

#新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷
贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共
享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共
享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''

#高级语言计算顺序
'''
    balance = balance + n

分两步：

    计算balance + n，存入临时变量中；
    将临时变量的值赋给balance。
    
你也不希望你的存款莫名其妙变成负数吧.
所以如果想要计算正确,就要给change_it()上一把锁当某个线程开始执行
change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时
执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由
于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以
，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
'''

#但可能因为锁阻止了多线程并发执行，包含锁的代码只能单线程模式执行

#另外,由于多个所由于可以存在多个锁，不同的线程持有不同的锁，并试图
#获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执
#行，也无法结束，只能靠操作系统强制终止。

#--示例
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#由于Python历史遗留的GIL问题,如果一个线程满CPU
#基本上只能以单核来执行线程,如果想要实现彻底的多核线程
#要用C扩展


