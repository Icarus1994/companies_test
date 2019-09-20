# -*- coding: utf-8 -*-
# @Time : 2019-09-18 19:41
# @Author : icarusyu
# @FileName: max_ave.py
# @Software: PyCharm
def f():
    line = list(map(int,input().split()))
    n = line[0]
    k = line[1]
    arr = list(map(int,input().split()))
    if k >= n:
        return sum(arr)/n
    min_v,max_v = arr[0],arr[0]
    for i in range(k):
        min_v = min(min_v, arr[i])
        max_v = max(max_v, arr[i])
    p,q = 0,k
    sum1 = sum(arr[:k]) - min_v - max_v
    # print('dfd',sum1)
    res = sum1
    while q < n:
        if arr[k] > max_v:
            # 考虑了arr[p] = min_v
            sum1 = sum1 + max_v - arr[p]
            max_v = arr[k]
        elif arr[k] < min_v:
            sum1 = sum1 + min_v - arr[p]
            min_v = arr[k]
        else:
            sum1 = sum1 -arr[p] + arr[q]
        res = max(res, sum1)
        p += 1
        q += 1
        # print('max_v',max_v,'min_v',min_v,'sum1',sum1)
    return res/(k-2)
print(f())




