# -*- coding: utf-8 -*-
# @Time : 2019-10-18 18:58
# @Author : icarusyu
# @FileName: __init__.py.py
# @Software: PyCharm
def without7(i):
    while i>0:
        if i%10 == 7:
            return False
        else:
            i = i//10
    return True
def f():
    n = int(input())
    if n<3:
        return 'No Solution!'
    for i in range(1,n-1):
        if i%7 and without7(i):
            for j in range(1,n-i):
                if j%7 and without7(j) and (n-i-j)%7 and without7(n-i-j):
                    return str(i) + ' ' + str(j) + ' ' + str(n-i-j)
print(f())




