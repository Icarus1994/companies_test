# -*- coding: utf-8 -*-
# @Time : 2019-09-05 19:58
# @Author : icarusyu
# @FileName: 区间最值之和.py
# @Software: PyCharm
def f():
    n = int(input().strip())
    arr = input().split()
    if not arr:return 0
    # dp =[[0 for j in range(len(arr))] for i in range(len(arr))]
    sum = 0
    for i in range(n):
        for j in range(i,n):
            if i == j:
                sum = (sum + int(arr[i]))
                left = int(arr[i])
            else:
                left = max(left,int(arr[j]))
                sum = (sum + left)
                # left = max(left,int(arr[j]))
    return sum % 1000000007
print(f())

def f1():
    n = int(input().strip())
    arr = input().split()
    if not arr: return 0
    # dp =[[0 for j in range(len(arr))] for i in range(len(arr))]
    sum = 0





