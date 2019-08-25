# -*- coding: utf-8 -*-
# @Time : 2019-08-23 21:53
# @Author : icarusyu
# @FileName: 2018_疯狂序列.py
# @Software: PyCharm
import sys
def f():
    n = int(sys.stdin.readline().strip())
    sum =0
    for i in range(1,n):
         sum += i
         if sum >=n:break
    print(i)
# f()
import  math
def f2():
    n = int(sys.stdin.readline().strip())
    # k = int((2*n-9/4)**0.5 + 0.5)
    k = math.ceil((2*n-0.25)**0.5-0.5)
    print(k)
f2()

# 题目： https://www.nowcoder.com/question/next?pid=10630581&qid=163496&tid=26488992

# 思路1
# 暴力求解，能解80%样例

# 思路2
# 等差数列：数组中有1个1，2个2，k个k，当选定值k时，数组中所有值为k的元素对应的位置范围为[k*(k-1)*0.5+1,k*(k+1)*0.5]
# 另右区间等于n,反过来求k，


