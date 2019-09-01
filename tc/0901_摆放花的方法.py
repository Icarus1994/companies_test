# -*- coding: utf-8 -*-
# @Time : 2019-09-01 20:44
# @Author : icarusyu
# @FileName: 0901_摆放花的方法.py
# @Software: PyCharm
import sys
import math
from itertools import *
def f():
    line1 = sys.stdin.readline().split()
    t,k = int(line1[0]),int(line1[1])
    tmp = {}
    for i in range(t):
        line = sys.stdin.readline().split()
        a, b = int(line[0]), int(line[1])
        cnt = 0
        for i in range(a,b+1):
            if i in tmp:
                cnt += tmp[i]
                continue
            if i < k:cnt+=1
            else:
                beishu = i//k
                for j in range(beishu+1):
                    num = i - j*k + j
                    cnt = (cnt + len(list(combinations(list(range(num)),j))) )%(math.e**9+1)
                tmp[i] = cnt
        print(cnt)
f()

# 问题
# 小明要摆花，有白花和红花两种，要求红花连续摆放的数量是输入k的整数倍（可以是0）,问
# 给出范围[a,b],求长度为a,a+1,...,b时共有多少种摆花方法

# case:0%，复杂度过高
