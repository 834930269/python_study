
# coding: utf-8

# In[6]:

class Student(object):
    pass
s=Student()
s.name='Michael'
print(s.name)

#还可以尝试给实例绑定一个方法：
def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#绑定方法
s.set_age(25)
print(s.age)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2=Student()
#s2.set_age(25)


# In[8]:

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score=score
Student.set_score=set_score
#给class绑定方法后，所有实例均可调用：
s.set_score(20)
s2.set_score(30)
print(s.score,s2.score)


# In[9]:

#使用__slots__

#但是，如果我们想要限制实例的属性怎么办？比如，
#只允许对Student实例添加name和age属性。

#为了达到限制的目的，Python允许在定义class的时候，
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s=student()
s.name='Michael'
s.age=8
#s.score=20#AttributeError


# In[10]:

#使用__slots__要注意，__slots__定义的属性仅
#对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(student):
    pass
g = GraduateStudent()
g.score=9999#没抛异常


# In[ ]:



