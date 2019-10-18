# -*- coding: utf-8 -*-
# @Time : 2019-09-12 11:05
# @Author : icarusyu
# @FileName: gcd.py
# @Software: PyCharm
def gcd(a,b):
    if a ==b:
        return a
    elif a <b:
        a,b = b,a
    while b:
        a,b = b, a%b
    return a








# 问题 辗转相除法求最大公约数
# 对数a，b,求得a%b，再让除数除以余数，一直到余数为0为止，此时的余数就是最大公约数
