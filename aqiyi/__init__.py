# -*- coding: utf-8 -*-
# @Time : 2019-09-08 16:00
# @Author : icarusyu
# @FileName: stone.py.py
# @Software: PyCharm
import itertools

def f():
    n = int(input())
    arr = input().split()
    lst = list(itertools.permutations(list(range(1,n+1)), n))
    for i in range(len(arr)):
        if arr[i] == '1':
            j = 0
            right = len(lst)
            while j < right:
                if lst[j][i] <= lst[j][i+1]:
                    lst.pop(j)
                    right -= 1
                else: j+=1
        else:
            j = 0
            right = len(lst)
            while j < right:
                if lst[j][i] >= lst[j][i+1]:
                    lst.pop(j)
                    right -=1
                else:  j +=1
    return (len(lst)) % (10**9+7)


print(f())