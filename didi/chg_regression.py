# -*- coding: utf-8 -*-
# @Time : 2019-08-27 20:08
# @Author : icarusyu
# @FileName: chg_regression.py
# @Software: PyCharm
def f():
    num = int(input())
    raw = input().split()
    num = []
    suan = []
    res = []
    for i in range(0,len(raw)-2,2):
        num.append(raw[i])
        suan.append(raw[i+1])
    num.append(raw[-1])

    i = 0
    start = 0 if suan[0] == '+' or suan[0] =='*' else 1
    while 1:
        # 负数字符串大小能正确比较吗
        while i< len(suan) and suan[i] == '+':
            i +=1
        end = i if suan[i] == '*' or suan[i] == '/' else i+1
        res.extend(sorted(num[start:end]))
        start = i if suan[i] == '*' else i+1

        while i< len(suan) and suan[i] == '-':
            i += 1
        end = i if suan[i] == '*' or suan[i] == '/' else i + 1
        res.extend(sorted(num[start:end]))
        start = i if suan[i] == '*' else i + 1

        while i< len(suan) and suan[i] == '*':
            i+=1
        end = i+1
        res.extend(sorted(num[start:end]))
        start = i+1

        while i< len(suan) and suan[i] == '/':
            i+=1
        end= i+1
        res.extend(sorted(num[start:end]))
        start = i+1
    ans = ''
    for i in range(len(res)-1):
        ans += res[i] + ' ' + suan[i] + ' '
    return ans + res[-1]

print(f())
# 题目
# 给出一个表达式，允许重复若干次这种行为：
# 当相邻两个数字交换时如果不改变表达式的值大小，则可以交换。
# 求当重复这种行为若干次后字典序最小的表达式

# 输入：数字个数n和表达式，表达式中数字和加减乘除用空格隔开，没有0,只有正整数和负整数
#
