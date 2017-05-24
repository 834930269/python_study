classmates=['Michael','Bob','Tracy']
print(classmates)
print('%s:%d' % ('返回classmates的个数',len(classmates)))
classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
print('删除list末尾元素: '+classmates.pop())
print(classmates)
print('删除list指定位置元素: '+classmates.pop(1))
print(classmates)
classmates[1]='Sarah'
print('将1替换成\'Sarah\':')
print(classmates)
L=['Apple',123,True]
print(L)
s=['python','java',['asp','php'],'scheme']
print(s)
print(len(s))
print('取出s[2][1]: '+s[2][1])
L=[]
print(len(L))