# -*- coding: utf-8 -*-
# @Time : 2019-10-18 20:19
# @Author : icarusyu
# @FileName: 3.py
# @Software: PyCharm
from itertools import combinations
def f():
    n,t = list(map(int,input().split()))
    arr = []
    res = 0
    for i in range(n):
        arr.append(list(map(int,input().split())))
        arr[i].append(arr[i][0]+ arr[i][1])
    arr.sort(key = lambda t:t[3],reverse=True)
    time = 0
    i = 0
    while i < (len(arr)):
        time += arr[i][2]
        if time > t:
            break
        else:
            i+=1
    arr = arr[:i]
    if i < len(arr):
        rest = t - (time - arr[i][2])
    else:
        rest = 0
    arr.sort(key=lambda t:t[2]/t[1],reverse=True)
    # print(arr)
    res = 0
    start = 0
    for i in range(len(arr)):
        res += (start+rest) * arr[i][1] + arr[i][0]
        start += arr[i][2]
    return res
print(f())






