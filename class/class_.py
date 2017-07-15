
# coding: utf-8

# In[13]:

class student(object):
    #绑定实例属性
    #__init__方法的第一个参数永远是self,即实例本身
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s: %s" % (self.name,self.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
        
bart=student('Bart Simpson',59)
print(bart.name,bart.score,bart)
bart.print_score()
print(bart.get_grade())


# In[14]:

#另一种访问方式
def pt_score(std):
    print('%s: %s' % (std.name,std.score))
pt_score(bart)


# In[19]:

'''
要定义一个方法，除了第一个参数是self外，其他
和普通函数一样。要调用一个方法，只需要在实例
变量上直接调用，除了self不用传递，其他参数正常传入：
'''

'''
和静态语言不同，Python允许对实例变量绑定任何数据，也就
是说，对于两个实例变量，虽然它们都是同一个类的不同实例，
但拥有的变量名称都可能不同：
'''
bart = student('Bart Simpson', 59)
lisa = student('Lisa Simpson', 87)
bart.age = 8
print(bart.age)
print(lisa.age)#抛异常


# In[ ]:



