
# coding: utf-8

# In[2]:

#Partial function包含在functools中
#int可以将字符串转换成整形
print('十进制: ',int('123456'),'\n')


# In[12]:

#但int()函数还提供额外的base参数，默认值为10。
#如果传入base参数，就可以做N进制的转换：
print('十六进制转十进制: ',int('E123456',16),'\n')


# In[13]:

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)
#非常麻烦，于是，我们想到，可以定义一个int2()的函数，默
#认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
print('二进制转十进制: ',int2('1000000'))
print('二进制转十进制: ',int2('1010101'))


# In[14]:

#functools.partial就是帮助我们创建一个偏函数的，不需要我
#们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3=functools.partial(int,base=2)
print('二进制转十进制: ',int3('1000000'))
print('二进制转十进制: ',int3('1010101'))


# In[22]:


'''
创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int, base=2)

实际上固定了int()函数的关键字参数base，也就是：

int2('10010')

相当于：

kw = { 'base': 2 }
int('10010', **kw)

当传入：

max2 = functools.partial(max, 10)

实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)

相当于：

args = (10, 5, 6, 7)
max(*args)

'''

max2 = functools.partial(max)
args = (10, 5, 6, 7)
print(max2(*args))
#out:10
max3 = functools.partial(max,102)
args = (10, 5, 6, 7)
print(max3(*args))
#OUT:102



