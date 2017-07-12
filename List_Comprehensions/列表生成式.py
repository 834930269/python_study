
# coding: utf-8

# In[1]:

#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
li=list(range(1,11))
print(li)


# In[2]:

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)


# In[3]:

#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
R=[x*x for x in range(1,11)]
print(R)


# In[12]:

#for循环后还可以加上if这样我们就可以筛出仅偶数的平方
#x&x-1是判断x是否是2的幂，x&1为1为奇
R=[x*x for x in range(1,11) if not(x&1)]
print(R)


# In[14]:

#还可以使用两层循环，可以生成全排列：
T=[m+n for m in 'ABC' for n in 'XYZ']
print(T)


# In[2]:

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
OS=[d for d in os.listdir('.')]# os.listdir可以列出文件目录
print(OS)
# Out [1]: ['.anaconda', '.android', '.bash_history', '.conda', '.condarc', '.gem', '.gemrc', '.gitconfig', '.idlerc', '.ipynb_checkpoints', '.ipython', '.jupyter', '.oracle_jre_usage', '.packettracer', '.ssh', '.viminfo', '360驱动大师.lnk', 'ACDSee5.lnk', 'AppData', 'Application Data', 'Cisco Packet Tracer 6.2sv', 'Contacts', 'Cookies', 'Desktop', 'Documents', 'Downloads', 'fancy_deboss.png', 'Favorites', 'fontawesome-webfont.svg', 'IntelGraphicsProfiles', 'Links', 'Local Settings', 'Music', 'My Documents', 'NetHood', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf', 'NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'ntuser.pol', 'Pictures', 'PrintHood', 'Recent', 'Saved Games', 'Searches', 'SendTo', 'Templates', 'Test.ipynb', 'Videos', 'wc', 'WebpageIcons.db', 'WIN7激活工具', 'XT.DAT.LOG1', 'XT.DAT.LOG2', 'xt.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf', 'xt.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms', 'xt.DAT{016888bd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms', '「开始」菜单', '列表生成式.ipynb', '宽带连接.lnk', '迭代.ipynb', '迭代.py']


# In[3]:

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)


# In[5]:

#因此,列表生成式也可以用两个变量生成list:
dp=[k+'='+v for k,v in d.items()]
print(dp)


# In[6]:

#最后把一个list中的字母全变成小写:
L=['Hello','World','IBM','Apple']
Lp=[s.lower() for s in L]
print(Lp)


# In[7]:

#使用内建的isinstance(key,type)可以判断key是否是type
#例:
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[k.lower() for k in L1 if isinstance(k,str)]
print(L2)


# In[ ]:



