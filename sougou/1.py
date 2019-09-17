# -*- coding: utf-8 -*-
# @Time : 2019-09-16 19:02
# @Author : icarusyu
# @FileName: 1.py
# @Software: PyCharm
def f():
    line0 = list(map(int,input().split()))
    m,n,d = line0[0],line0[1],line0[2]
    train = []
    test = []
    a = 0
    for i in range(m):
        train.append(list(map(int, input().split())))
        if train[-1][0] == 1:
            a +=1
    p_1 = a/m # p(Y=1)
    # print('p_1',p_1)
    for j in range(n):
        t = input().split()
        test.append(t[1:])

    pos = {i:{} for i in range(d)}
    neg = {i:{} for i in range(d)}
    N = [0 for i in range(d)]
    P = [0 for i in range(d)]
    for i in range(m):
        if train[i][0] == 1:
            for j in range(1,d+1):
                if train[i][j] not in pos[j-1]:
                    pos[j-1][train[i][j]] = 1
                else:
                    pos[j-1][train[i][j]] += 1
        else:
            for j in range(1,d+1):
                if train[i][j] not in neg[j-1]:
                    neg[j-1][train[i][j]] = 1
                else:
                    pos[j-1][train[i][j]] += 1
    for i in pos:
        for k,v in pos[i].items():
            pos[i][k] = (v+1)/(v + a )
    for i in neg:
        for k,v in neg[i].items():
            # print(k,v,m-a)
            neg[i][k] = (k + 1)/(v + m-a)

    for i in range(d):
        N[i] = len(neg[i])
        P[i] = len(pos[i])

    # print(pos,neg)
    for i in range(n):
        # 判断正样本概率
        p_pos = p_1
        for j in range(d):
            if test[i][j] not in pos[j]:
                p_pos *=1/(a + P[j])
            else:
                p_pos *= pos[j][test[i][j]]
        p_neg = 1-p_1
        for j in range(d):
            if test[i][j] not in neg[j]:
                p_neg = 1/(m-a + N[j])
            else:
                p_neg *= neg[j][test[i][j]]
        # print('P_pos',p_pos)
        # print('p_neg',p_neg)

        if p_pos>= p_neg:
            print(1)
        else:
            print(0)

f()

