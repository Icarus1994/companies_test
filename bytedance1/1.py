# -*- coding: utf-8 -*-
# @Time : 2019-10-20 19:37
# @Author : icarusyu
# @FileName: 1.py
# @Software: PyCharm
from collections import defaultdict

def get_father(v):
    if father[v] == v:
        return v
    else:
        father[v] = get_father(father[v])
        return father[v]

n,m = list(map(int,input().split()))
vals = [0] + list(map(int,input().split()))
r = [list(map(int,input().split())) for i in range(m)]
father = [i for i in range(n+1)]
d = defaultdict(int)

for a,b in r:
    fa,fb = get_father(a), get_father(b)
    if fa<fb:
        father[fa] = fb
        # vals[fa] += vals[fb]
    else:
        father[fb] =fa
        # vals[fb] +=vals[fa]
# print(max(vals))
for i in range(1,n+1):
    d[father[i]] += vals[i]
print(max(d.values()))

