#Thread-较量级线程

#建议在多线程环境下用局部变量,但传递变量传递很麻烦

'''
def process_student(name):
    std=Student(name)
    #std是局部变量,但是每个函数都要用它,因此必须传过去
    #一层一层的传
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_1(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
'''
#考虑,以每层的thread对象作为key,值为操作对象

class Student:
    def __init__(self,name):
        self.name=name

global_dict = {}
def std_thread(name):
    std=Student(name)
    #吧std放到全局变量中dict中
    global_dict[threading.current_thread()]=std
    do_task_1()
    do_task_2()
def do_task_1():
    #不传入std,而是根据当前线程查找
    std=global_dict[threading,current_thread()]
    #...
def do_task_2():
    #任何函数都可以根据当前线程查找
    std=global_dict[threading,current_thread()]
    #...

#ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事
import threading
#创建全局ThreadLocal对象:
local_school=threading.local()
def process_student():
    #获取当前县城关联的student
    std=local_school.student
    print('Hello,%s (in %s)\n' % (std,threading.current_thread().name))
def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('Alice',),name='Thread_A')
t2=threading.Thread(target=process_thread,args=('Bob',),name='Thread_B')
t1.start()
t2.start()
t1.join()
t2.join()

#ThreadLocal解决了线程锁的问题,把所有的变量都处理成局部变量,互不影响
