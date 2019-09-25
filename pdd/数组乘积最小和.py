# -*- coding: utf-8 -*-
# @Time : 2019-09-25 15:05
# @Author : icarusyu
# @FileName: 数组乘积最小和.py
# @Software: PyCharm
def f():
    n,m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    for i in range(m):
        sum += arr[i] * arr[2*m-1 - i]
    print(sum)

f()