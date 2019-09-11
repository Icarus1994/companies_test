# -*- coding: utf-8 -*-
# @Time : 2019-09-11 16:08
# @Author : icarusyu
# @FileName: 0911_用最少的箱子装货（有bug）.py
# @Software: PyCharm
def f():
    n = int(input())
    ex = list(map(int,input().split()))
    v = list(map(int,input().split()))
    # v相同ex不同的情况
    tup = []
    for i in range(n):
        tup.append((v[i],i))
    tup.sort(key= lambda t:t[0])
    # print('tup',tup)
    delta = []
    sum = 0
    for i in range(n):
        index = tup[i][1]
        delta.append(v[index] - ex[index])
        sum += delta[i]
    # print(delta)
    move = 0
    for i in range(n):
        if move > sum/2:
            break
        move += delta[i]
    print(n-i,' ',move - delta[i-1])

# print(f())

f()