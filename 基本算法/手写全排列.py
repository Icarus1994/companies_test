# -*- coding: utf-8 -*-
# @Time : 2019-09-18 16:34
# @Author : icarusyu
# @FileName: 手写全排列.py
# @Software: PyCharm
def f(arr,start,end):
    if start == end:
        print(arr)
    for i in range(start,end+1):
        # 交换start和i下标的值时，相当于确定某排列此时第start个位置的元素，因此start位置元素也要和自己交换
        arr[start],arr[i] = arr[i],arr[start]
        f(arr,start+1,end)
        arr[start],arr[i] = arr[i],arr[start]
a = ['a','b','c']
f(a,0,2)

# 参考：https://blog.csdn.net/qq_31601743/article/details/82053201
