# -*- coding: utf-8 -*-
# @Time : 2019-09-17 20:48
# @Author : icarusyu
# @FileName: 2.py
# @Software: PyCharm
def f():
    line = list(map(int,input().split()))
    a,b,c = line[0],line[1],line[2]
    n = line[4]
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n == 3:
        return c
    elif n == 4:
        return
    i= 0
    while i < n-3:
        d = a +b+c
        # t = d
        a = b
        b = c
        c = d
        i +=1
        print(a,b,c,d)
    return d
print(f())

