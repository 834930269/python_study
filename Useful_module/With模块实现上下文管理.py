
# coding: utf-8

# In[1]:

'''
with,是可以自动实现关闭与开始的语法.比如关闭文件和开启文件

任何对象，只要正确实现了上下文管理，就可以用于with语句。

实现上下文管理是通过__enter__和__exit__这两个方法实现的。
例如，下面的class实现了这两个方法：
'''

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)
        
#这样我们就可以把自己写的资源对象用于with语句：
with Query('Bob') as q:
    q.query()


# In[2]:




# In[ ]:



