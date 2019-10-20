
# -*- coding: utf-8 -*-
# @Time : 2019-10-20 20:36
# @Author : icarusyu
# @FileName: 2.3.py
# @Software: PyCharm
#!/usr/bin/env python
# encoding: utf-8
'''
@author: 12064
@software: PyCharm
@project:LeetCode
@file: 三角形.py
@time: 2019/10/20 19:54
@site:
'''

if __name__ == "__main__":
    mod = 1e9 + 7
    n = int(input())

    # base = 1
    # temp_b = 1<<(n-1)
    # temp_b = int(temp_b % mod)
    #
    # temp_a = 1 << (2 * n - 1)
    # temp_a = int(temp_a % mod)
    #
    # res = int((temp_b + temp_a) % mod)
    # print(res)

    #快速幂求x ^ y
    n2 = n*2 - 1
    n1 = n - 1
    base = 2
    a = 1

    res = 0
    while n1 > 0:
        cur = n1 % 2
        if cur == 1:
            a *= base
            a = int(a % mod)
        if n1 > 0:
            base = base * base
            base = int(base % mod)
        n1 = n1 >> 1


    res += a
    a = 1
    base = 2
    while n2 > 0:
        # print("n2 = ", n2)
        # print("a = ",a, " base = ", base)
        cur = n2 % 2
        if cur == 1:
            a *= base
            a = int(a % mod)
        base = base * base
        base = int(base % mod)
        n2 = n2 >> 1
    res += a
    res= int(res%mod)
    print(res)



