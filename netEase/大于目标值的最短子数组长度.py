# -*- coding: utf-8 -*-
# @Time : 2019-09-20 17:43
# @Author : icarusyu
# @FileName: 大于目标值的最短子数组长度.py.py
# @Software: PyCharm
def f():
    arr = list(map(int,input().split(',')))
    # print(arr)
    if len(arr) == 1:return 0
    cnt = 10004
    dp = [[0 for i in range(len(arr))]for j in range(len(arr))]
    for i in range(1,len(arr)):
        for j in range(i,len(arr)):
            if j-i+1 >= cnt:
                break
            dp[i][j] = dp[i][j-1] + arr[j]
            if dp[i][j] >= arr[0]:
                cnt = min(cnt, j-i +1)
                break
    return 0 if cnt == 10004 else cnt

print(f())


