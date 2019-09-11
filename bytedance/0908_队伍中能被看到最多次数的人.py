# -*- coding: utf-8 -*-
# @Time : 2019-09-08 19:15
# @Author : icarusyu
# @FileName: 0908_队伍中能被看到最多次数的人.py
# @Software: PyCharm
def f():
    n = int(input())
    arr = input().split()
    max_see = 0
    p = 0
    if not arr:return
    if n == 1:return int(arr[0])
    for i in range(n-2,0,-1):
        if int(arr[i]) == int(arr[i+1]):
            if max_see <=1:
                max_see = 1
                p = i
        elif int(arr[i]) > int(arr[i+1]):
            # 在arr[i+1]之前添加一个哨兵
            last = int(arr[i+1]) -1
            see = 0
            for j in range(i+1,n):
                if int(arr[j]) > int(arr[i]):
                    if see >= max_see:
                        max_see = see
                        p = i
                    break
                elif int(arr[j]) == int(arr[i]):
                    if see +1 >=max_see:
                        max_see = see
                        p = i
                    break
                elif int(arr[j]) < int(arr[i]) and int(arr[j]) > last:
                    see +=1
                    last = int(arr[j])
            # 当遍历到最后一个数但未更新时
            if j == n-1 and see >= max_see:
                max_see = see
                p = i
    return int(arr[p])
print(f())

# 问题
# 一堆不同身高的人排队，后面的人只能直视前方（不能斜向上也不能斜向下），如果前面的人和他一样高或者比他高
# 那么他能看到前面的人。
# 求队伍中被看到人数最多的第一个人的身高

# 分析
# 要求第一个人，可以从后往前遍历，然后更新相应数据
# 两层循环，外层i从队列末尾往前遍历，判断i和i+1个元素的大小关系，当arr[i] <= arr[i+1]时，情况很简单
# 当arr[i] > arr[i+1]时，那么内层从i+1往后遍历，直到遇到大于等于arr[i]的，那么第I个人被看到的次数不再更新
