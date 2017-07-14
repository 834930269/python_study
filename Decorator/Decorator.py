
# coding: utf-8

# In[1]:

#函数也是一个对象,所以可以赋值给变量
def now():
    print('1997-02-10')
f=now
f()


# In[3]:

#函数对象有一个__name__属性,可以拿到其名字
print(f.__name__)


# In[5]:

'''
现在，假设我们要增强now()函数的功能，比如，
在函数调用前后自动打印日志，但又不希望修改
now()函数的定义，这种在代码运行期间动态增
加功能的方式，称之为“装饰器”（Decorator）。
'''
#本质上，decorator就是一个返回函数的高阶函数
#。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
'''
观察上面的log，因为它是一个decorator，所以接受
一个函数作为参数，并返回一个函数。我们要借助
Python的@语法，把decorator置于函数的定义处：

调用now()函数，不仅会运行now()函数本身，还会在
运行now()函数前打印一行日志：
'''
@log
def now2():
    print('1997-12-11')
now2() 


# In[16]:

#把@log放到now()函数的定义处，相当于执行了语句：
#now=log(now)
'''
1.wrapper()函数的参数定义是(*args, **kw)，因此，
wrapper()函数可以接受任意参数的调用。在wrapper()
函数内，首先打印日志，再紧接着调用原始函数。

2.如果decorator本身需要传入参数，那就需要编写一个返
回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

'''
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
#这个3层嵌套的decorator用法如下：
@log2('execute')
def now3():
    print('2015-3-25')
now3()
#三层嵌套是这样的:now = log('execute')(now)


# In[17]:

'''
我们来剖析上面的语句，首先执行log('execute')，
返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。
因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数
，它们的__name__已经从原来的'now'变成了'wrapper'：
'''
print(now.__name__)


# In[20]:

'''
因为返回的那个wrapper()函数名字就是'wrapper'，所以，
需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的，所以，一个
完整的decorator的写法如下：
'''
import functools

def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
#或者针对带参数的decorator：
def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# In[22]:

#题目
'''
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
OOP的装饰模式需要通过继承和组合来实现，而Python除了能支
持OOP的decorator外，直接从语法层次支持decorator。Python
的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使
用起来非常灵活和方便。

请编写一个decorator，能在函数调用的前后打印出'begin call'
和'end call'的日志。


再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
    
又支持：

@log('execute')
def f():
    pass
'''
def log5(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('args1 num =%d' %len(args1))
            print('begin %s():' % func.__name__)
            func()
            print('end %s().\n' % func.__name__)
        return wrapper
    return decorator

@log5('123','a')
def dream():
    print('My Dream.')

@log5()
def future():
    print('Must..')
    
dream()
future()

'''
Out:
args1 num =2
begin dream():
My Dream.
end dream().

args1 num =0
begin future():
Must..
end future().
'''
        


# In[ ]:



