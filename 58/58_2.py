# -*- coding: utf-8 -*-
# @Time : 2019-10-13 20:45
# @Author : icarusyu
# @FileName: 58_2.py.py
# @Software: PyCharm

# 未通过测试样例
def f():
    m,n,k = list(map(int,input().split()))
    c =[]
    for i in range(m,n+1):
        c.append(i)
    res = 0
    while sum(c)>0:
        i = 0
        while i<len(c) and str(c[i])[0] != str(k):
            c[i] = c[i] - int(str(c[i])[0]) * (10** (len(str(c[i])) -1))
            i+=1
        j = i
        while j<len(c) and str(c[j])[0] == str(k):
            c[j] = c[j] - int(str(c[j])[0]) * (10 ** (len(str(c[j]) )-1))
            j+=1
        print(i,j)
        res =res+ j-i
        while j<len(c):
            c[j] = c[j] - int(str(c[j])[0]) * (10 ** (len(str(c[j]) )+1))
            j += 1
    return res
print(f())

