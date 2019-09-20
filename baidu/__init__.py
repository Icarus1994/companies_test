# -*- coding: utf-8 -*-
# @Time : 2019-09-17 20:09
# @Author : icarusyu
# @FileName: stone.py.py
# @Software: PyCharm
def f():
    line = list(map(int,input().split()))
    n,m = line[0],line[1]
    door = []
    ball = []
    if m == 0 or n == 0:
        print(0)
        return
    for i in range(n):
        door.append((list(map(int, input().split()))) )
    for i in range(m):
        ball.append(int(input()))
    ball.sort()
    door.sort(key = lambda t:t[0])
    i = 0
    while i+1 < len(door):
        if door[i][1] >= door[i+1][0]:
            door[i][1] = max(door[i][1], door[i+1][1])
            door.pop(i+1)
        else:
            i+=1

    # print('door',door)

    sum = 0
    k = 0
    for j in range(len(door)):
        while k < len(ball):
            if ball[k] < door[j][0]:
                pass
            if ball[k] >= door[j][0] and  ball[k] <= door[j][1]:
                sum +=1
                # k+=1
            if ball[k] > door[j][1]:
                break
            k +=1
    print(sum)
f()
