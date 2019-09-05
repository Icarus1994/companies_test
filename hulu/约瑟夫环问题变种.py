# -*- coding: utf-8 -*-
# @Time : 2019-09-05 19:18
# @Author : icarusyu
# @FileName: 约瑟夫环问题变种.py.py
# @Software: PyCharm
def f():
    line1 = input().split()
    n, m = int(line1[0]),int(line1[1])
    arr = input().split()
    w = input().split()
    j = 0
    for i in range(2,n+1):
        j = (j+ m)%i
    # j为出局人的下标
    sum = 0
    ans = 0
    for k in range(len(arr)):
        sum += int(w[k])
        ans += int(arr[(k + j) % len(arr)]) * int(w[k])
    # return round(float(ans/sum), 5)
    # print("%.5f", ans/sum)


print(f())
# f()
