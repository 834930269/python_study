
# coding: utf-8

# In[3]:

#__str__
class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__=__str__
s=student('Michael')
#__str__是控制打印时输出类型,__repr__是控制台直接s输出的类型
#如果不重写,那会输出<__main__.Student object at 地址>
s
print(s)


# In[10]:

#__iter__
'''
如果一个类想被用于for ... in循环，类似list或tuple那样，就必
须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python
的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个
值，直到遇到StopIteration错误时退出循环。

斐波那契:
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for i in Fib():
    print(i)
    


# In[14]:

#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，
#但是，把它当成list来使用还是不行
#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
f=Fib()
print(f[0],f[1],f[2],f[100])
'''
但是list有个神奇的切片方法：

>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]

对于Fib却报错。原因是__getitem__()传入的参数
可能是一个int，也可能是一个 切片对象slice ，所以要做判断：

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
        if isinstance(n, slice): # n是切片
'''
print(f[:20])#但是没有判断倒序切片以及没有对step参数作处理：

'''
此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以
作key的object，例如str。

与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋
值。最后，还有一个__delitem__()方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的
list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”
，不需要强制继承某个接口。
'''


# In[18]:

#__getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#调用name属性，没问题，但是，调用不存在的score属性，就有问题了
'''
>>> s = Student()
>>> print(s.name)
Michael
>>> print(s.score)
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'score'
错误信息很清楚地告诉我们，没有找到score这个attribute。

要避免这个错误，除了可以加上一个score属性外，Python还有另
一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
返回函数也是完全可以的：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
只是调用方式要变为：

>>> s.age()
25
注意，只有在没有找到属性的情况下，才调用__getattr__，
已有的属性，比如name，不会在__getattr__中查找。

此外，注意到任意调用如s.abc都会返回None，这是因为我们
定义的__getattr__默认返回就是None。要让class只响应特定
的几个属性，我们就要按照约定，抛出AttributeError的错误：
raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
'''
s=Student()
print(s.name,s.score,s.age())


# In[19]:

'''
举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

    http://api.server/user/friends
    http://api.server/user/timeline/list

如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：
'''
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
#try
print(Chain().status.user.timeline.list)
#out[]: /status/user/timeline/list

#这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，
#而且，不随API的增加而改变！

#还有些REST API会把参数放到URL中，比如GitHub的API：
#GET /users/:user/repos

#调用时，需要把:user替换为实际用户名。


# In[21]:

#__call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s()


# In[29]:

print(callable(max),callable(map),callable(str),callable('123'))


# In[ ]:



