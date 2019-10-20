# -*- coding: utf-8 -*-
# @Time : 2019-10-20 19:13
# @Author : icarusyu
# @FileName: 3.py
# @Software: PyCharm
def gcd(a,b):
    if a==b:
        return a
    elif a<b:
        a,b = b,a
    while b:
        a,b = b,a%b
    return a

def ad(a,x,y):
    return (a*y + x,y)

def f():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    if n==1:
        print(arr[0],'1',)
        return
    x,y = 1,arr.pop()
    # x,y = ad(arr.pop(), 1,y)
    while len(arr)>0:
        y,x = ad(arr.pop(), x, y)
        # print('test',x,y)
    if y%x==0:
        print(y//x,1)
        return
    else:
        m = gcd(y,x)
        print(y//m,x//m)
        return

f()

