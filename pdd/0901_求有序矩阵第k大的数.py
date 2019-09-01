# -*- coding: utf-8 -*-
# @Time : 2019-09-01 16:14
# @Author : icarusyu
# @FileName: 0901_求有序矩阵第k大的数.py
# @Software:
import heapq
class solution:
    def __init__(self):
        self.heap=[]

    def f(self):
        line = input().split()
        n,m ,k= int(line[0]),int(line[1]), int(line[2]) # 行，列
        arr = {}
        for i in range(n):
            heapq.heappush(self.heap,(-1)*(i+1)*m)
            if (-1)*(i+1)*m not in arr:
                arr[(-1)*(i+1)*m] = [(i,m-1)]
            else:
                arr[(-1) * (i + 1) * m].append((i,m-1))
        while k>1:
            v = heapq.heappop(self.heap)
            # print('v',v)
            # print('arr[v]',arr[v])
            p = arr[v].pop()
            new_v = (p[0] + 1) * p[1]
            if (-1)*new_v not in arr:
                arr[(-1)*new_v] = [(p[0],p[1]-1)]
            else:
                arr[(-1)*new_v].append((p[0],p[1]-1))
            # print('arr',arr)
            heapq.heappush(self.heap,(-1)*new_v)
            k -= 1
        return (-1)*heapq.heappop(self.heap)
print(solution().f())

