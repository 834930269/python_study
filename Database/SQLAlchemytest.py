
# coding: utf-8

# In[1]:

#这个库是操作ORM的
#ORM：Object-Relational Mapping
#导入
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# In[2]:

#创建对象的基类
Base=declarative_base()
#定义user对象
class User(Base):
    #表的名字
    __tablename__='user'
    
    #表的结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    
#初始化数据库连接
engine=create_engine('mysql+mysqlconnector://root:zwt~19970210@localhost:3306/test')
#创建DBSession类型
DBSession=sessionmaker(bind=engine)

#create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：

#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'


# In[4]:

#由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

#创建session对象:
session=DBSession()
#创建新User对象
new_user=User(id='5',name='Bob')
#添加到Session
session.add(new_user)
#提交即保存到数据库
session.commit()
#关闭session
session.close()


# In[6]:

#创建session
session=DBSession()
#创建Query查询,filter是where条件,最后调用one返回唯一行,如果调用all()则返回所有行
user=session.query(User).filter(User.id=='5').one()
#打印类型和对象的name属性
print('type:',type(user))
print('name:',user.name)
#关闭session
session.close()


# In[ ]:

'''
数据库之间的联系这样来做:

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
    
ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
'''

