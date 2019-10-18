# -*- coding: utf-8 -*-
# @Time : 2019-10-18 11:15
# @Author : icarusyu
# @FileName: 排序算法.py
# @Software: PyCharm

# 快排递归
def quickSort(arr):
    if not arr:return
    return qSort(arr,0,len(arr)-1)

def qSort(arr,l,r):
    if l<r:
        index = partion(arr,l,r)
        qSort(arr,l,index-1)
        qSort(arr,index+1,r)
    return arr

def partion(arr,l,r):
    privot = arr[l]
    # 快排不断赋值的过程，就是一开始将从右边往左遍历时第一个小于等于privot的值挖空，赋值给arr[l]
    # 依次执行
    while l<r:  # 易错
        while l<r and arr[r]>= privot: # 易错
            r-=1
        arr[l] = arr[r]
        while l<r and arr[l]< privot:
            l+=1
        arr[r] = arr[l]
    arr[l] = privot
    return l

# 快排非递归：使用栈保存需排序的子数组左右下标对
def quickSort1(arr):
    if not arr:return
    stack = [(0,len(arr)-1)]
    while stack:
        l,r = stack.pop()
        if l<r:
            index = partion(arr,l,r)
            stack.append((l,index-1))
            stack.append((index+1,r))
    return arr




