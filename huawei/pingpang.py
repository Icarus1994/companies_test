# -*- coding: utf-8 -*-
# @Time : 2019-09-25 19:24
# @Author : icarusyu
# @FileName: pingpang.py
# @Software: PyCharm
def f():
    t = int(input())
    for i in range(t):
        tian = int(input())
        arr = list(map(int,input().split()))
        max_v = 0
        final = 0
        out = [arr[0]]
        for j in range(1,len(arr)):
            # l,r = 0,0
            k = 0
            while k < len(out):
                if arr[j] < out[k]:
                    final = final + k - (len(out) - k)
                    max_v = max(max_v, final)
                    out.insert(k,arr[j])
                    print('1',final)
                    break
                elif arr[j] == out[k]:
                    p = k
                    while p < len(out):
                        if arr[j] < out[p]:
                            break
                        else:
                            p+=1
                    final = final + k - (len(out) - p)
                    max_v = max(max_v, final)
                    # print('2',final)
                    if p < len(out):
                        out.insert(p,arr[j])
                    else:
                        out.append(arr[j])
                    break
                else:
                    k +=1
            if k == len(out):
                final = final + len(out)
                max_v = max(max_v, final)
                # print('3',final)
                out.append(arr[j])
        # print('out',out)
        print(max_v,final)

# f()
def f1():
    t = int(input())
    for i in range(t):
        tian = int(input())
        arr = list(map(int, input().split()))
        res = [0 for j in range(100006)]
        max_v = 0
        final = 0
        max_val = 0
        for j in range(len(arr)):
            max_val = max(max_val, arr[j])
            final = final + sum(res[:arr[j]]) - sum(res[arr[j]+1 : max_val+1])
            max_v = max(max_v,final)
            res[arr[j]] +=1
        print(max_v,final)

f1()

# 问题
# 小明训练乒乓球n天，每天有一个失误次数。计算第t天的分数时，会先继承前一天的分数，在此基础上按如下规则更新：
# 前面每有一天失误次数大于当天失误次数，则分数—1；
# 前面每有一天失误次数小于当天失误次数，则分数+1；
# 相等时则不影响
# 第1天时分数为0
# 输入第一行为t,表示有t组数据
# 之后每两行中，第一行表示训练天数，第二行表示每天训练时失误次数，
# 输出为训练时得到的最大分数和训练完n天后得到的分数