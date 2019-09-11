# -*- coding: utf-8 -*-
# @Time : 2019-09-08 19:58
# @Author : icarusyu
# @FileName: 三杯水倒水量体积.py
# @Software: PyCharm
import sys
def f():
    line = input().split()
    a,b,c,k = int(line[0]),int(line[1]), int(line[2]), int(line[3])
    que = []
    # 虽然题目里认为是无限多的水，但是其实所有水的范围是：[一杯盛满水,三个杯子都盛满水]
    que.append((a,0,0,1))
    que.append((0,b,0,1))
    que.append((0,0,c,1))

    que.append((a,b,0,1))
    que.append((a,0,c,1))
    que.append((0,b,c,1))

    que.append((a,b,c,1))

    while len(que) > 0:
        now = que[0]
        que.pop(0)
        for i in range(3):
            if now[i] == k:
                return now[3]

        s = now[0] + now[1] + now[2]
        if s == k:
            return now[3]

        for i in range(3):
            if s - now[i] == k:
                return now[3]

        # 1-2
        a_minus=min(b - now[1], now[0])
        new_b = now[1] + a_minus
        new_a = now[0] - a_minus
        if (new_a, new_b, now[2], now[3] +1) not in que:
            que.append((new_a, new_b, now[2], now[3]+1))

        # 1-3
        a_minus = min(c-now[2], now[0])
        new_c = now[2] + a_minus
        new_a = now[0] - a_minus
        if (new_a, now[1], new_c, now[3]+1) not in que:
            que.append((new_a, now[1], new_c, now[3]+1))

        # 2-1
        b_minus = min(a-now[0], now[1])
        new_a = now[0] + b_minus
        new_b = now[1] - b_minus
        if (new_a,new_b,now[2], now[3]+1) not in que:
            que.append((new_a,new_b,now[2], now[3]+1))

        # 2-3
        b_minus = min(c-now[2], now[1])
        new_c = now[2] + b_minus
        new_b = now[1] - b_minus
        if (now[0], new_b, new_c, now[3]+1) not in que:
            que.append((now[0], new_b, new_c, now[3]+1))

        # 3-1
        c_minus = min(a-now[0], now[2])
        new_a = now[0] + c_minus
        new_c = now[2] - c_minus
        if (new_a, now[1], new_c, now[3]+1) not in que:
            que.append((new_a, now[1], new_c, now[3]+1))

        # 3-2
        c_minus = min(b-now[1], now[2])
        new_b = now[1] + c_minus
    return -1

print(f())

# 问题
# 给3杯水，只知道三个杯子的容量，水有无限多，操作可以为：将水盛满；将水倒空；水杯之间相互倒水（但是要求一个杯子被倒空或者一个杯子被倒满）
# 求最少经过多少次可以利用杯子量处指定体积的水，如果无法通过这种方式量出则返回-1

# 思路
# 对初始所有可能的情况设置相应个数的根节点，利用队列做bfs,一步一步倒水，每次倒水产生一个子节点（在现有基础上多了子情况）
# 存在的问题：
# 1、没有考虑无法量出指定刻度的情况
# 2、三个杯子中水的总量是一定的，没有考虑某个杯子盛有不到一杯水时把水倒掉或者倒满的情况



