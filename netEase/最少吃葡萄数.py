# -*- coding: utf-8 -*-
# @Time : 2019-09-21 16:10
# @Author : icarusyu
# @FileName: 最少吃葡萄数.py
# @Software: PyCharm
def f():
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        arr.sort()
        sum = arr[2]
        for i in range(arr[1] +1):
            for j in range(arr[2] +1):
                if i + j >= sum:
                    break
                a1 = i + j - (arr[1] - i)
                a2 = i + j - (arr[2] - j)
                if a1 + a2 >= arr[0]:
                    sum = min(sum, i + j)
        print(sum)
# print(f())
f()

# 问题
# 有a,b,c 3种葡萄，第一个人只吃a,b葡萄，第二个人只吃b,c葡萄，第3个人只吃a,c葡萄
# 现在给了每种葡萄的数量，要求把葡萄吃完并让吃的最多的那个人吃的葡萄数尽可能少，
# 求吃葡萄最多的人吃葡萄的最小值