# -*- coding: utf-8 -*-
# @Time : 2019-09-11 15:48
# @Author : icarusyu
# @FileName: 0911_最长公共子串.py
# @Software: PyCharm
def f():
    m = int(input())
    a = input().split()
    n = int(input())
    b = input().split()
    last = [0 for i in range(n+1)]
    cur = [0 for i in range(n+1)]
    cnt = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                cur[j] = last[j-1] + 1
                cnt = max(cnt, cur[j])
            else:
                cur[j] = 0
        # print('last',last)
        # print('cur',cur)
        last = cur
        cur = [0 for k in range(n+1)]
    return cnt
print(f())


