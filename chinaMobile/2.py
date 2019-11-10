# -*- coding: utf-8 -*-
# @Time : 2019-10-24 19:45
# @Author : icarusyu
# @FileName: 2.py
# @Software: PyCharm
def f():
    n = int(input())
    tmp = set()
    while n>0:
        nex = input()
        if nex[-5:] not in tmp:
            tmp.add(nex[-5:])
            # print(tmp)
            print('6' +nex[-5:])
        else:
            print('000000')
        n-=1
f()
