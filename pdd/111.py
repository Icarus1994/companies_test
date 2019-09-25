# -*- coding: utf-8 -*-
# @Time : 2019-09-25 16:53
# @Author : icarusyu
# @FileName: 111.py
# @Software: PyCharm



if __name__ == "__main__":
    n,m,k = list(map(int,input().split()))

    dp = []
    for i in range(n+1):
        temp = []
        for j in range(m+1):
            temp.append(0)
        dp.append(temp)
    dp[0][0] = 1
    for i in range(1,n+1):
        dp[i][0] = 1
    for j in range(1,m+1):
        dp[0][j] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for b in range(m+1):
        for a in range(n+1):
            if dp[a][b] >= k :
                break
    n1 = a
    m1 = b
    ret = []
    for i in range(a + b):
        if n1 > 0 and k <= dp[n1-1][m]:
            ret.append('a')
            n1 -= 1
        else:
            if n1 > 0:
                k -= dp[n1-1][m1]
            ret.append('b')
            m1 -= 1
    ret = ''.join(ret)
    print(ret)


