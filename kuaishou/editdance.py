# -*- coding: utf-8 -*-
# @Time : 2019-09-16 20:59
# @Author : icarusyu
# @FileName: editdance.py
# @Software: PyCharm
def f():
    a = input()
    b = input()
    if not a:
        return len(b)
    if not b :
        return len(a)
    dp = [[0 for i in range(len(a) +1)] for j in range(len(b)+1)]
    for i in range(1,len(a)+1):
        dp[0][i] = i
    for i in range(1,len(b)+1):
        dp[i][0] = i

    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if a[j-1] == b[i-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] +1, dp[i-1][j] +1)
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) +1
    return dp[-1][-1]


print(f())