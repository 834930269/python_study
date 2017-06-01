# --*--coding:gbk--*--

import re

fp = open("data1.txt","r")
f = open("in.txt","w")

cnt=0

while True:
    
    s = fp.readline()
    
    aList = re.findall('([-+]?\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?',s) #使用正规表达式搜索字符串
    
    if len(s) == 0:
        break
    if len(aList) == 2:
        print >> f,'I'
    if len(aList) == 3:
        print >> f,'O'
    for ss in aList:
        print >> f, ss[0]+ss[2],
        
    print >> f, ''
    cnt=cnt+1
fp.close()
