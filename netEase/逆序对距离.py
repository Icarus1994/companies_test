
# -*- coding: utf-8 -*-
# @Time : 2019-09-21 15:32
# @Author : icarusyu
# @FileName: 逆序对距离.py
# @Software: PyCharm
def f():
    n = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                sum += j-i
    return sum

print(f())