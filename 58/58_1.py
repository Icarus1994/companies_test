# -*- coding: utf-8 -*-
# @Time : 2019-10-13 21:31
# @Author : icarusyu
# @FileName: 58_1.py
# @Software: PyCharm
def f():
    arr = list(map(int,input().split()))
    n,m = arr[0],arr[1]
    arr1 = []
    dic = {}
    for i in range(2,len(arr)):
        if arr[i] in dic:
            dic[arr[i]]+=1
        else:
            arr1.append(arr[i])
            dic[arr[i]] = 1
    arr1.sort()
    # print(arr1)
    # return arr1
    i = 0
    while i < m:
        print(arr1)
        dic[arr1[1]] -=1
        if dic[arr1[1]] ==0:
            s1 = arr1.pop(1)
        dic[arr1[0]] -=1
        if dic[arr1[0]] ==0:
            s2 = arr1.pop(0)
        if s1+s2 in dic:
            dic[s1+s2] +=1
        else:
            dic[s1+s2] = 1
        if s1+s2 not in arr1:
            arr1.append(s1+s2)
            arr1.sort()
        i+=1
    return arr1[0]
print(f())

# 通过76%
