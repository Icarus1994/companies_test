# -*- coding: utf-8 -*-
# @Time : 2019-08-31 16:47
# @Author : icarusyu
# @FileName: xinlang.py
# @Software: PyCharm
def f():
    arr = input().split(',')
    if not arr or len(arr) == 1:return 0
    list.sort(arr)
    cnt,pre = 0, int(arr[0])
    for i in range(1,len(arr)):
        add = 0
        if int(arr[i]) > pre:
            add = pre - int(arr[i]) +1
        pre = add + int(arr[i])
        cnt += add
    return cnt
print(f())