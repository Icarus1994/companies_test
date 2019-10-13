# -*- coding: utf-8 -*-
# @Time : 2019-10-13 21:04
# @Author : icarusyu
# @FileName: 58_3.py
# @Software: PyCharm
def f():
    n = int(input())
    if n<=1:return 1
    l,r = 1,2
    i =0
    while i < n-2:
        l,r = r,l+r
    return r