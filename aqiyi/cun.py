# -*- coding: utf-8 -*-
# @Time : 2019-09-08 16:37
# @Author : icarusyu
# @FileName: 0908_队伍中能被看到最多次数的人.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.lst = []
        self.cnt =0
        self.arr = None
    def f(self):
        n = int(input())
        self.arr = input().split()
        ls = list(range(n))
        self.digui(ls, 0,n-1)
        return self.cnt

    def digui(self, ls,start, end):
        if start >= end:
            fg = True
            for i in range(len(self.arr)):
                if self.arr[i] == '1':
                    if ls[i] > ls[i+1]:continue
                    else:
                        fg = False
                        break
                else:
                    if ls[i] < ls[i+1]:continue
                    else:
                        fg = False
                        break
            if fg:self.cnt +=1
        else:
            for i in range(start,end +1):
               ls[start],ls[i] = ls[i], ls[start]
               self.digui(ls,start+1,end)
               ls[start],ls[i] = ls[i], ls[start]

print(solution().f())