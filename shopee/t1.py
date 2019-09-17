# -*- coding: utf-8 -*-
# @Time : 2019-08-21 21:30
# @Author : icarusyu
# @FileName: t1.py.py
# @Software: PyCharm
import sys
class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.matrix = None
        self.cnt = 0
    def f(self):
        arr1 = sys.stdin.readline().split()
        self.x,self.y,n = int(arr1[0]),int(arr1[1]),int(arr1[2])
        self.matrix = [[0 for i in range(self.y+1)] for j in range(self.x+1)]
        for i in range(n):
            line = sys.stdin.readline().split()
            self.matrix[int(line[0])][int(line[1])] = 1
        self.dfs(0,0)
        return self.cnt

    def dfs(self,x,y):
        if x == self.x and y == self.y:
            self.cnt+=1
            return
        if x+1 < len(self.matrix[0]) and self.matrix[x+1][y] ==0:
            self.dfs(x+1,y)
        if y+1 < len(self.matrix) and self.matrix[x][y+1]==0:
            self.dfs(x,y+1)

print(Solution().f())