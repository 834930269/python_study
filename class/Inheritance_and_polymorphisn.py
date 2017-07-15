
# coding: utf-8

# In[5]:

'''
在OOP程序设计中，当我们定义一个class的时候，可以从某个
现有的class继承，新的class称为子类（Subclass），而被继
承的class称为基类、父类或超类（Base class、Super class）。
'''
#比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...')
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass
class Cat(Animal):
    pass
'''
对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是
它的子类。Cat和Dog类似。

继承有什么好处？最大的好处是子类获得了父类的全部功能。由
于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什
么事也没干，就自动拥有了run()方法：
'''
dog=Dog()
dog.run()
cat=Cat()
cat.run()

#当子类和父类都存在相同的run()方法时，我们说，
#子类的run()覆盖了父类的run()，在代码运行的时候，
#总是会调用子类的run()。这样，我们就获得了继承的
#另一个好处：多态。
class Puppy(Animal):
    def run(self):
        print('Puppy is running...')
class Shark(Animal):
    def run(self):
        print('Shark is running...')
puppy=Puppy()
puppy.run()


# In[7]:

#判断一个变量是否是某个类型可以用isinstance()判断：
#可以发现,puppy可以使Animal也可以是Puppy.
print(isinstance(puppy,Animal))
print(isinstance(puppy,Puppy))
b=Animal()
print(isinstance(b,Puppy))
#所以，在继承关系中，如果一个实例的数据类型是某个子类
#，那它的数据类型也可以被看做是父类。但是，反过来就不行：


# In[12]:

#要理解多态的好处，我们还需要再编写一个函数，这个函数接受
#一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog())
run_twice(Puppy())
run_twice(Shark())


# In[ ]:

'''
多态的好处在于:

新增一个Animal的子类，不必对  --run_twice()--  
做任何修改，实际上，任何依赖Animal作为参数的函
数或者方法都可以不加修改地正常运行，原因就在于
多态。

著名的“开闭”原则：

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。



对于静态语言（例如Java）来说，如果需要传入Animal类型，则
传入的对象必须是Animal类型或者它的子类，否则，将无法调用
run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一
个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看
做是鸭子。
'''

