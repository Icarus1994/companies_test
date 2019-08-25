# -*- coding: utf-8 -*-
# @Time : 2019-08-24 11:59
# @Author : icarusyu
# @FileName: test.py
# @Software: PyCharm
def f():
    s = input()
    n, m = int(s.split()[0]), int(s.split()[1])
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for j in range(m):
        line = input().split()
        print(line)
        # line = input()
        # print(line, '\n',line.split())
        if line[0] == '1':
            print('')
        elif line[0] == '2':
            sum = 0
            for k in range(int(line[1]) - 1, int(line[2])):
                sum += arr[k]
            print(sum)
        else:
            max_v = arr[int(line[1])]
            for k in range(int(line[1]) - 1, int(line[2])):
                max_v = arr[k] if arr[k] > max_v else max_v
            print(max_v)

f()