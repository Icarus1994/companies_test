# -*- coding: utf-8 -*-
# @Time : 2019-09-05 20:19
# @Author : icarusyu
# @FileName: 通过迷宫的最少翻墙次数.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.mstep = 10000
        self.n = 0
        self.matrix = None
    def f(self):
        n = int(input())
        self.matrix = [[] for i in range(n)]
        self.n = n
        for i in range(n):
            self.matrix[i] = input().split()
        self.go(0,0,0)
        return self.mstep

    def go(self,x,y,s):
        if x == self.n-1 and y == self.n-1:
            self.mstep = min(self.mstep,s)
            return
        if x+1 < self.n:
            s = s+1 if self.matrix[x+1][y] == '1' else s
            if s >= self.mstep:
                return
            self.go(x+1,y,s)
        if y+1 < self.n:
            s = s+1 if self.matrix[x][y+1] == '1' else s
            if s >= self.mstep:
                return
            self.go(x,y+1,s)
print(solution().f())
