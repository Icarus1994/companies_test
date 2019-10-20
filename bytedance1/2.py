# -*- coding: utf-8 -*-
# @Time : 2019-10-20 19:29
# @Author : icarusyu
# @FileName: 2.py
# @Software: PyCharm
# def f():
#     n = int(input())
#     zheng = 1
#     ni = 0
#     while n>0:
#         zheng, ni = 3*zheng + ni, zheng + 3*ni
#         # print(zheng,ni)
#         n-=1
#     return zheng % (10**9+7)

# def f():
#     n = int(input())
#     # if n==1:return 3
#     i = n+1
#     j = 2
#     res = 1
#     while i >1:
#         # print('last',res)
#         res = 4*res - 2**(j-2)
#         j+=1
#         # print('tt',2**(i-2))
#         # print('res',res)
#         i-=1
#     return res %(10**9+7)
# def mi(n):
#     # 快速幂求x ^ y
#     n2 = n * 2 - 1
#     n1 = n - 1
#     base = 2
#     a = 1
#     mod = 1e9+7
#     res = 0
#     while n1 > 0:
#         cur = n1 % 2
#         if cur == 1:
#             a *= base
#             a = int(a % mod)
#         if n1 > 0:
#             base = base * base
#             base = int(base % mod)
#         n1 = n1 >> 1
#     return n1
def mi(base,n):
    mod = 1e9+7
    res = 1
    a = 1
    while n>0:
        cur = n%2
        if cur==1:
            a = int((a*base) % mod)
        base = int((base * base)%mod)
        n= n>>1
    return res

def f():
    n = int(input())
    a = mi(2,n)
    print(a)
    res = (a + a*a)//2 % (1e9+7)
    return res
print(f())