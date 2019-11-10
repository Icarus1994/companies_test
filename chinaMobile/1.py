# -*- coding: utf-8 -*-
# @Time : 2019-10-24 15:54
# @Author : icarusyu
# @FileName: 1.py.py
# @Software: PyCharm
import math
def f():
    while 1:
        l,r = list(map(int,input().split()))
        if l ==0 and r ==0:return
        if f1(l,r):
            print('OK')
        else:
            print('Sorry')


def f1(l,r):
    for i in range(l, r + 1):
        if f2(i ** 2 + i + 41):
            pass
        else:
            return False

    return  True

def f2(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True

f()