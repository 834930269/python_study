
# coding: utf-8

# In[2]:

'''
还记得装饰器（decorator）可以给函数动态加上功能吗？
对于类的方法，装饰器一样起作用。Python内置的@property
装饰器就是负责把一个方法变成属性调用的：
'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''
@property的实现比较复杂，我们先考察如何使用。把一个getter方
法变成属性，只需要加上@property就可以了，此时，@property本身
又创建了另一个装饰器@score.setter，负责把一个setter方法变成属
性赋值，于是，我们就拥有一个可控的属性操作：

相当于 Get Set
'''
a=Student()
a.score = 60 # OK，实际转化为a.set_score(60)
print(a.score)# OK，实际转化为s.get_score()


# In[3]:

#a.score=9999  ValueError('score must between 0 ~ 100!')
#还可以定义只读属性，只定义getter方法，不定义setter方法
#就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
#上面的birth是可读写属性，而age就是一个只读属性，因为age
#可以根据birth和当前时间计算出来。

'''
练习

请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self.width*self.height
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


# In[ ]:


