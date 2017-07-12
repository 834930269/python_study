# -*- coding: utf-8 -*-

def triangles():
    L=[1]
    while True:
        yield L
        l=len(L)
        R=[1]
        for i in range(1,l):
            R.append(L[i-1]+L[i])
        R.append(1)
        L=R[:]
'''
第二种解法,中间为中间列表,和上面一样,只不过直接加起来了,避免了中间变量
def triangles():
l = [1] 
while True:
    yield l 
    l = [1] + [l[i]+l[i+1] for i in range(len(l)-1)] + [1]
'''
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
