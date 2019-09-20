# -*- coding: utf-8 -*-
# @Time : 2019-09-18 19:10
# @Author : icarusyu
# @FileName: stone.py.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.step = 100000

    def f(self):
        n = int(input())
        arr = list(map(int, input().split()))
        self.dump(arr,0,n-1,0)
        return self.step

    def dump(self,arr,start,end,step):
        if start == end:
            if step < self.step:
                self.step = step
            return
        if step >= self.step:
            return

        for i in range(start+1,end+1):
            if arr[i] == arr[start]:
                self.dump(arr,i,end,step+1)
                break
        self.dump(arr,start+1,end,step+1)


print(solution().f())
