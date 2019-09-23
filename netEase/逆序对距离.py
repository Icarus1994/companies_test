
# -*- coding: utf-8 -*-
# @Time : 2019-09-21 15:32
# @Author : icarusyu
# @FileName: 逆序对距离.py
# @Software: PyCharm
def f():
    n = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                sum += j-i
    return sum

print(f())

# 算法复杂度过大，a 60%
# 问题
# 给定一个数组a，若i<j时有a[i]>a[j],距离为|i-j|
# 求数组中所有逆序对距离之和

# 相关知识
# 归并排序求逆序数对
# 一个数组的逆序数对等于左子数组的逆序数对+右子数组的逆序数对+横跨左右数组的逆序数对