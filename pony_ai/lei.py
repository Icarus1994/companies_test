# -*- coding: utf-8 -*-
# @Time : 2019-09-18 20:37
# @Author : icarusyu
# @FileName: lei.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.num = 0

    def f(self):
        turn = int(input())
        for i in range(turn):
            row = int(input())
            arr = []
            for j in range(row):
                arr.append(list(map(int,input().split())))
            p = 1
            no_zero = (row//2 + row %2)**2
            self.count(arr, row, 0,0,no_zero,0, row**2-no_zero)
            print(self.num)
            self.num = 0

    def count(self,arr,row,x,y,no_zero,step,stop):
        if step == stop:
            if no_zero == 0:
                self.num +=1
            return
        # q_num = row**2-no_zero
        p = 1
        self.count(arr,row,x+2,y+2,no_zero,step+1,stop)
        if x>0:
            arr[x-1][y] -=1
            if arr[x-1][y] == 0:
                no_zero -=1
        if x < row-1:
            arr[x+1][y] -=1
            if arr[x+1][y] ==0:
                no_zero -=1
        if y >0:
            pass
