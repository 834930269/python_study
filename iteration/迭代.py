
# coding: utf-8

# In[2]:

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)


# In[5]:

for ch in 'ABC':
    print(ch)


# In[1]:

#判断是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


# In[8]:

for i,value in enumerate(['A','B','C']):
    print(i,value)
print(enumerate(['A','B','C']))
#enumerate是枚举,列举的意思
#如果对于一个列表,既要遍历索引又要遍历元素时,首先可以这样写
list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print(i ,list1[i])
print('\n')
#但这样很麻烦,所以可以用enumrate这样写
for i,value in enumerate(list1):
    print(i,value)
print('\n')
#enumerate还可以接受第二个参数,用于指定初始索引
for i,value in enumerate(list1,1):
    print(i,value)
print('\n')


# In[9]:

#在for循环里,同时引用两个变量
for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)


# In[ ]:

#end

