# -*- coding: utf-8 -*-
# @Time : 2019-09-16 21:19
# @Author : icarusyu
# @FileName: zhishu.py
# @Software: PyCharm
import math
def f():
    n = int(input())
    arr = [0,0]
    # if n <3:return arr[n-1]
    for i in range(2,n+1):
        # 是合数
        if simple_cnt(i):
            for k in range(2, int(math.sqrt(i))+1):
                if i % k ==0:
                    # print(i/k)
                    arr.append(arr[k] + arr[i//k])
                    break
        else:arr.append(1)
    # print(arr)
    return sum(arr)


def simple_cnt(num):
    fg = False
    i = 2
    while i <= int(math.sqrt(num)):
        if num % i ==0:
            fg = True
            break
        i +=1
    return fg
print(f())
# print(simple_cnt(4))

