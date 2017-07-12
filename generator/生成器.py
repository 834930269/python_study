# coding: utf-8

# In[1]:

'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，
创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元
素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制
，称为生成器：generator。
'''
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L=[x*x for x in range(10)]
print(L)
g=(x*x for x in range(10))
print(g)
#out[1]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#out[2]: <generator object <genexpr> at 0x0000000004C2FB48>


# In[3]:

'''
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
generator必须紧跟着输入,否则用next()只能输出一次循环

'''
g=(x*x for x in range(10))
i=0
while i<10:
    print(next(g))
    i+=1


# In[10]:

#用for
g=(x*x for x in range(10))
for n in g:
    print(n)


# In[6]:

#斐波那契
#注意,赋值语句 a,b=b,a+b
#相当于 
'''
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]

'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
fib(6)
#可以注意到,上面那个函数和generator很相似,他与generator只差一步之遥


# In[18]:

#只需要把print改成yield即可
'''
这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就
返回。而变成generator的函数，在每次调用next()的时候
执行，遇到yield语句返回，再次执行时从上次返回的yield
语句处继续执行。
'''
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib2(6)
print(f)
#Out[3]: <generator object fib2 at 0x0000000004C2FDB0>
#想要在循环中得到fib2的return值,必须捕获StopIteration错误返回值包括在
#其中的value中
while True:
    try:
        x=next(f)
        print('f:',x)
    except StopIteration as ev:
        print('Generator return value:',ev.value)
        break


# In[17]:

#yield举例
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o=odd()
print('之前没输出')
for n in o:
    print(n)


# In[ ]:

#test
'''
杨辉三角定义如下：

          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
'''
def triangles():
    L=[1]
    while True:
        yield L
        l=len(L)
        R=[1]
        for i in range(1,l):
            R.append(L[i-1]+L[i])
        R.append(1)
        L=R[:]
'''
第二种解法,中间为中间列表,和上面一样,只不过直接加起来了,避免了中间变量
def triangles():
l = [1] 
while True:
    yield l 
    l = [1] + [l[i]+l[i+1] for i in range(len(l)-1)] + [1]
'''
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

