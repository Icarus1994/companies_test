# -*- coding: utf-8 -*-
# @Time : 2019-10-09 19:55
# @Author : icarusyu
# @FileName: 58_2.py.py
# @Software: PyCharm
def f():
    n = int(input())
    if n == 1:
        return 6
    meter = [0] *n
    meter[0] = meter[1] = 3
    for i in range(2,n):
        meter[i] = meter[i-1] + meter[i-2]
    res = 0
    for j in range(n-1,-1,-1):
        res = 2*(res + meter[j])
    return res
print(f())