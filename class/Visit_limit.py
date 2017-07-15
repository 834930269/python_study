
# coding: utf-8

# In[3]:

'''
如果要让内部属性不被外部访问，可以把属性的名称前加上
两个下划线__，在Python中，实例的变量名如果以__开头，
就变成了一个私有变量（private），只有内部可以访问，外
部不能访问，
'''
class student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))
'''
改完后，对于外部代码来说，没什么变动，但是已经无法从外部
访问实例变量.__name和实例变量.__score了:只能通过类内的方法
才可以调用这些私有变量
'''
bart = student('Bart Simpson', 98)
bart.print_score()
print(bart.__name)
    


# In[4]:

'''
如果外部想要获取name和score怎么办,
给student类添加get_name和get_score
外部想要修改怎么办,set_score

需要注意的是，在Python中，变量名类似__xxx__的，
也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
特殊变量是可以直接访问的，不是private变量，所以，不能用
__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name
，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，
请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量：
'''
print(bart._student__name)#好神奇
#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。


# In[5]:

#所以如果外界对实例化对象设置私有变量的值,因为上面说了
#私有变量会被改名为 _student__name这样,所以如果使用
#bart.__name='New Name',则表示在该对象内新建一个变量
#不影响本来的__name
bart.__name='New name'
bart.print_score()
#out[]: Bart Simpson: 98


# In[ ]:



