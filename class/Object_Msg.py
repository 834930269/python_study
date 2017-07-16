
# coding: utf-8

# In[1]:

#type()
print(type(123))
print(type('str123'))
print(type(None))
print(type(abs),type(123)==type(456),type(123)==int,type('abc')==type(123))


# In[2]:

import types
#对象是否是函数
def fn():
    pass
print(type(fn)==types.FunctionType,type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType,type((x for x in range(10)))==types.GeneratorType)


# In[3]:

#isinstance
print(isinstance(b'a', bytes))
#还可以判断一个变量是否是某些类型中的一种，比如
#下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


# In[7]:

'''
如果要获得一个对象的所有属性和方法，可以使用dir()函数
，它返回一个包含字符串的list，比如，获得一个str对象的
所有属性和方法：
'''
print(dir(fn),'\n','\n',dir('abc'))


# In[11]:

#len()
print(len('ABC'))
#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class Mydog(object):
    def __len__(self):
        return 100
print(len(Mydog()))
#lower
print('ABC'.lower())


# In[5]:

#仅仅把属性和方法列出来是不够的，配合getattr()、
#setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(setattr(obj, 'y', 19)) # 设置一个属性'y'
print(getattr(obj, 'y')) # 获取属性'y'
#如果试图获取不存在的属性，会抛出AttributeError的错误：
print(getattr(obj, 'z'))# 获取属性'z'


# In[14]:

#可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404


# In[12]:

#也可以获得对象的方法：
print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'
fn = getattr(obj, 'power')# 获取属性'power'并赋值到变量fn
print(fn,'\n',fn())# 调用fn()与调用obj.power()是一样的


# In[ ]:



