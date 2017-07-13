
# coding: utf-8

# In[2]:

#我们先看map。map()函数接收两个参数，一个是函数，
#一个是Iterable，map将传入的函数依次作用到序列的
#每个元素，并把结果作为新的Iterator返回。

#现在,我们用python代码实现1-9映射到x^2
def f(x):
    return x*x
r=map(f,[x for x in range(10)])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结
#果r是一个Iterator，Iterator是惰性序列，因此通过
#list()函数让它把整个序列都计算出来并返回一个list。


# In[3]:

#将数字转换成字符
print(list(map(str,[x for x in range(1,10)])))


# In[4]:

#reduce
'''
再看reduce的用法。reduce把一个函数作用在一个序列
[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce
把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
当然,可以直接用sum()
'''
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[x for x in range(1,10)]))


# In[5]:

#如果将[1，3，5，7，9]变成13579
def fn(x,y):
    return x*10+y
print(reduce(fn,[x for x in range(1,10,2)]))


# In[6]:

'''
这个例子本身没多大用处，但是，如果考虑到字符串
str也是一个序列，对上面的例子稍加改动，配合map()，
我们就可以写出把str转换为int的函数：
'''
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))


# In[7]:

#也可以直接返回转换结果
def str2int(s):
    return reduce(fn, map(char2num, s))
print(str2int('98661'))


# In[9]:

#还可以用lambda函数进一步转化，事实证明Python的整数运算是大数= =
#当然,可以直接用int()
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('46131346431311616131'))


# In[10]:

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
#其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：
#['Adam', 'Lisa', 'Bart']：
def normalize(name): 
    return name[0].upper()+name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# In[11]:

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()
#函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# In[20]:

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    n,l=s.find('.'),len(s)
    if n!=-1:
        return reduce(lambda x,y:x*10+y,map(lambda x:int(x),s[:n]))+reduce(lambda x,y:x/10+y,map(lambda x:int(x)/10,s[l-1:n:-1]))
    else:
        return reduce(lambda x,y:x*10+y,map(lambda x:int(x),s))
print('str2float(\'166516516.1133165\') =', str2float('166516516.1133165'))


# In[ ]:



