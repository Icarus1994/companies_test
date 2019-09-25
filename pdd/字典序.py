# -*- coding: utf-8 -*-
# @Time : 2019-09-25 16:10
# @Author : icarusyu
# @FileName: 字典序.py
# @Software: PyCharm
def f():
    n,m,k = list(map(int,input().split()))
    if k <=n:
        res = ''
        for i in range(k):
            res += 'a'
        return res
    ans = []
    s = ''
    for i in range(n+1):
        s +='a'
        for j in range(1,m+1):
            s += 'b'
            ans.append(s)
    ans.sort()
    return ans[k-n-1]
print(f())