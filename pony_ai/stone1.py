# -*- coding: utf-8 -*-
# @Time : 2019-09-18 20:16
# @Author : icarusyu
# @FileName: stone1.py
# @Software: PyCharm
def f():
    n = int(input())
    arr = list(map(int, input().split()))
    dp =[0 for i in range(n)]
    # dp[0] = 1
    for i in range(1,n):
        color = dp[i-1]
        for j in range(i-1,-1, -1):
            if arr[i] == arr[j]:
                color = dp[j]
                break
        dp[i] = min(color,dp[i-1]) +1
    return dp[-1]

print(f())
# 青蛙跳石头问题，递归a40%，动态规划a 80%
