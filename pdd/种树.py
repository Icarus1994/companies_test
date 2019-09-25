# -*- coding: utf-8 -*-
# @Time : 2019-09-25 15:14
# @Author : icarusyu
# @FileName: 种树.py
# @Software: PyCharm
def f1():
    n,m = list(map(int, input().split()))
    arr = [False for i in range(n)]
    tree = []
    sum = 0
    for i in range(m):
        tree.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(tree[i][0]-1,tree[i][1]):
            if arr[j] == False:
                sum +=1
                arr[j] = True
        print(sum)

f1()


