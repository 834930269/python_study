
# coding: utf-8

# In[15]:

from enum import Enum
Month=Enum('Months',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)


# In[17]:

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import unique
@unique
class WeekDay(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复值。
day1=WeekDay.Mon
print(day1)
print(WeekDay['Tue'])
print(WeekDay.Tue.value)
print(day1 == WeekDay.Mon)
print(day1 == WeekDay.Tue)
print(WeekDay(1))

for name,member in WeekDay.__members__.items():
    print(name,'=>',member,member.value)


# In[ ]:



