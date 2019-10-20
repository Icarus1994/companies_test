# -*- coding: utf-8 -*-
# @Time : 2019-10-18 19:31
# @Author : icarusyu
# @FileName: 4.py
# @Software: PyCharm
def f():
    n,m,k = list(map(int,input().split()))
    init = list(map(int,input().split()))
    before = []
    for i in range(m):
        before.append((chr(i+65),init[i]))
    # before = before[:k]
    for i in range(1,n):
        cur = list(map(int,input().split()))
        now = []
        for q in range(len(cur)):
            for p in range(len(before)):
                now.append((before[p][0] + chr(q+65), before[p][1] + cur[q]))
        now.sort(key= lambda t:t[1],reverse=True)
        if k<len(now) and now[k-1][1] == now[k][1]:
            # new = now[k-1:]
            # new.sort(key=lambda t: t[0])
            # new.sort(key=lambda t: t[1], reverse=True)
            # before = now[:k-1].append(new[0])
            now.sort(key=lambda t: t[0])
            now.sort(key=lambda t: t[1], reverse=True)
            before = now[:k]
        else:
            before = now[:k]
        #
        # now.sort(key= lambda t:t[0])
        # now.sort(key = lambda t:t[1],reverse=True)
        # before = now[:k]
        # print(now)

    for x in range(len(before)):
        print(before[x][0])


f()