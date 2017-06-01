# -*- coding: gbk -*-

from pylab import *
import numpy as np  
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D
import re
fp = open("out2.txt","r")
cnt=0
x,y,z=[],[],[]
while True:
    li=[]
    s = fp.readline()
    if len(s) == 0:
        break
    aList = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s)
    for ss in aList:
        aNum = float((ss[0]+ss[2]))
        li.append(aNum)
        
    if len(li) == 3:
        x.append(float(li[0]))
        y.append(float(li[1]))
        z.append(float(li[2]))

# ax=subplot(111,projection='3d') #创建一个三维的绘图工程

# ax.scatter(x,y,z,c='r') #绘制数据点

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.plot_trisurf(x, y, z, cmap='rainbow')

ax.set_zlabel('Z') 
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
