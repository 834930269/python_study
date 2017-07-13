
# coding: utf-8

# In[1]:

print(sorted([36, 5, -12, 9, -21]))
#此外，sorted()函数也是一个高阶函数，它还可
#以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
#我们给sorted传入key--函数--，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# In[5]:

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#key是排序规则函数


# In[6]:

#按名字排序
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
#按成绩从高到低排序
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)


# In[ ]:



