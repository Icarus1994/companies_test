# -*- coding: utf-8 -*-
# @Time : 2019-09-01 15:03
# @Author : icarusyu
# @FileName: 0901_按优先级排列的数组.py
# @Software: PyCharm
class solution:
    def __init__(self):
        self.jishu = []
        self.oushu = []

    def f(self):
        inp = input()
        if not inp or inp.split(';') == 0 :return
        arr = inp.split(',')
        n, arr[-1] = arr[-1].split(';')[1],arr[-1].split(';')[0]
        for i in range(len(arr)):
            if int(arr[i]) % 2:
                self.jishu.append(int(arr[i]))
            else:
                self.oushu.append((int(arr[i])))
        self.oushu.sort(reverse = True)
        self.jishu.sort(reverse=True)
        self.oushu.extend(self.jishu)
        res = ''
        for i in range(int(n)):
            res = res + str(self.oushu[i]) + ','
        return res.strip(',')
        # if int(n) <= len(self.oushu):
        #     for i in range(int(n)):
        #         res = res + str(self.oushu[i]) + ','
        #     return res.strip(',')
        # else:
        #     for i in range(len(self.oushu)):
        #         res = res + str(self.oushu[i]) + ','
        #     for j in range(int(n) - len(self.jishu)):
        #         res = res + str(self.jishu[i]) + ','
        #     print('res',res)
        #     return res.strip(',')
print(solution().f())
        # res = ''
        # len_oushu = len(self.oushu)
        # if int(n) <= len(self.oushu):
        #     for i in range(int(n)):
        #         res += str(self.output(self.oushu))
        #     return res.strip(',')
        # else:
        #     for i in range(len(self.oushu)):
        #         res = res +  str(self.output(self.oushu))  + ','
        #     t = int(n)-len_oushu
        #     for i in range(len(self.jishu)):
        #         res = res + str(self.output(self.jishu)) + ','
        #
        # return res.strip(',')

    #
    # def insert(self,arr,ele):
    #     if len(arr) == 0:
    #         arr.append(ele)
    #         return arr
    #     arr.append(ele)
    #     i = len(arr)-1 # i是ele当前下标
    #     while i>0:
    #         if arr[(i+1)//2] < arr[i]:
    #             arr[i] = arr[(i+1)//2]
    #             arr[(i+1)//2] = ele
    #             i = (i+1)//2
    #         else:break
    #     return arr
    #
    # def output(self,arr):
    #     if not arr :return
    #     if len(arr) ==1:return arr.pop()
    #     ans = arr[0]
    #     arr[0] = arr[-1]
    #     arr.pop()
    #     i = 0
    #     while (i+1)*2 <= len(arr):
    #         if (i+1)*2 == len(arr):
    #             if arr[(i+1)*2-1] > arr[i]:
    #                 t = arr[i]
    #                 arr[i] = arr[2*i+1]
    #                 arr[2*i+1] = t
    #                 i = 2*i +1
    #             else:break
    #         else:
    #             max_v = max(arr[i],arr[2*i+1],arr[2*i+2])
    #             if max_v == arr[i]:break
    #             elif max_v == arr[2*i+1]:
    #                 t = arr[i]
    #                 arr[i] = arr[2*i+1]
    #                 arr[2*i+1] = t
    #                 i = 2*i+1
    #             else:
    #                 t = arr[i]
    #                 arr[i] = arr[2*i +2]
    #                 arr[2*i+2] = t
    #                 i = 2*i+2
    #     return ans
    #
    #
