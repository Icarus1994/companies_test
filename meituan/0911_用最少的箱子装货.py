# -*- coding: utf-8 -*-
# @Time : 2019-09-11 16:34
# @Author : icarusyu
# @FileName: 0911_用最少的箱子装货.py
# @Software: PyCharm
#!/usr/bin/env python
# encoding: utf-8


import sys

# sys.stdin = open("4.txt")

if __name__ == "__main__":
    n = int(input())
    an = list(map(int,input().split()))
    bn = list(map(int,input().split()))#容量
    index = list(range(n))
    # index = sorted(index,key = lambda i : bn[i],reverse=True)
    index = sorted(index,key = lambda i : (bn[i],an[i]),reverse=True)

    new_bn = []
    new_an = []
    for inde in index:
        new_bn.append(bn[inde])
        new_an.append(an[inde])
    del an
    del bn
    # print(new_bn)
    # print(new_an)
    all_things = sum(new_an)
    all_things2 = all_things
    num= 0
    i = 0
    while all_things > 0:
        all_things -=  new_bn[i]
        i+=1
        num += 1
    cost = 0
    for i in range(num):
        # cost += (new_bn[i] - new_an[i])
        cost += (min(new_bn[i],all_things2) - new_an[i])
        # print("cost = ",cost)
        # all_things -= (new_bn[i] - new_an[i])
        all_things2 -= new_bn[i]

    print(num,' ',cost)

# 问题
# 给定两个长度为n的数组，第一个为n个箱子中已有货物的数量（每个货物重量都为单位1），
# 第二个数组为每个箱子的容量
# 已知一个货物从原来所属箱子移动到另一箱子需要1s
# 求用最少箱子存储所有货物时，箱子的个数和相应的最少移动时间

# 思路
# 按箱子容量从小到大排序，对【每个箱子容量-已有货物】构成的数组delta按照容量排序的顺序重新排序
# 求delta元素之和sum,对delta从小到大遍历，当从0到当前元素之和sum2大于sum/2时，n-此时的下标i为最少箱子数目，sum2为移动时间
