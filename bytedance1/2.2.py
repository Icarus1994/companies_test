# -*- coding: utf-8 -*-
# @Time : 2019-10-20 20:11
# @Author : icarusyu
# @FileName: 2.2.py
# @Software: PyCharm


def f():
    n = int(input())
    mod = 1e9+7

    base = 1

    tb = 1<<(n-1)
    tb = int(tb%mod)

    ta = 1<<(2*n-1)
    ta = int(ta%mod)

    res = int((tb+ta)%mod)
    print(res)

f()