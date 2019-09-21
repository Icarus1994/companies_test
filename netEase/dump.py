# -*- coding: utf-8 -*-
# @Time : 2019-09-21 16:28
# @Author : icarusyu
# @FileName: dump.py
# @Software: PyCharm
def f():
    t = int(input())
    n,k = list(map(int, input()))
    arr = list(map(int, input()))
    ans = digui(arr,0,k,1)

def digui(arr,start,k,chance):
    if start == len(arr)-1:
        return True
    p = start+1
    high = arr[start+1]
    # for i in range(start+1,min(len(arr), start + k)):


