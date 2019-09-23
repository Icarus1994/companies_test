# -*- coding: utf-8 -*-
# @Time : 2019-09-21 16:10
# @Author : icarusyu
# @FileName: 最少吃葡萄数.py
# @Software: PyCharm
def f():
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        arr.sort()
        sum = arr[2]
        for i in range(arr[1] +1):
            for j in range(arr[2] +1):
                if i + j >= sum:
                    break
                a1 = i + j - (arr[1] - i)
                a2 = i + j - (arr[2] - j)
                if a1 + a2 >= arr[0]:
                    sum = min(sum, i + j)
        print(sum)
# print(f())
f()

# 问题
# 有a,b,c 3种葡萄，第一个人只吃a,b葡萄，第二个人只吃b,c葡萄，第3个人只吃a,c葡萄
# 现在给了每种葡萄的数量，要求把葡萄吃完并让吃的最多的那个人吃的葡萄数尽可能少，
# 求吃葡萄最多的人吃葡萄的最小值

# f()代码只a了30%，因为算法本身有问题。算法假设的是将每种葡萄数从小到大排列得到a1,b1,c1三个数，
# 吃的最多的人是吃b,c的那个人。但是其实有可能a1b1c1相近时，吃最多葡萄的人是吃ac,ab的人，这个不一定的
# 但是为什么能a一部分代码呢，因为测试样例中有30%的样例吃最多葡萄的是吃b,c葡萄的人或者恰好最多吃葡萄数与之相等

# 思路
# 仔细思索我们就会发现，如果较少的两堆葡萄足够某个人吃(即两堆葡萄之和大于等于总数的1/3)，
# 那么3个人可以平均分这些葡萄(当然啦，如果葡萄不能整除3，就再加上1，为啥？
# 因为别管是多1个葡萄还是多2个葡萄，都得+1(被一人吃和被两人吃，没区别))。
# 如果较少的两堆葡萄还不够某个人吃(那也不能再吃啦，因为一人只能吃两种葡萄)，
# 那么最大值就等于最多的那堆葡萄除以2，如果最大值是奇数，还得再加1.（因为肯定会有一人多吃一人少吃）
# 参考：https://blog.csdn.net/weixin_41687289/article/details/101150439
def f1():
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        arr.sort()
        ave = sum(arr)//3
        if arr[0] + arr[1] >=ave:
            if sum(arr) %3 == 0:
                print(sum(arr)/3)
            else:
                print(sum(arr)//3+1)
        else:
            if arr[2] %2 == 0:
                print(arr[2]//2)
            else:
                print(arr[2]//2+1)