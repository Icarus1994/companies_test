# -*- coding: utf-8 -*-
# @Time : 2019-10-09 20:04
# @Author : icarusyu
# @FileName: 2.py
# @Software: PyCharm
def f():
    s = input()
    res = 0
    i  =0
    while i < len(s):
        l = ord(s[i])
        fg = True
        enter = False
        while i<len(s) and s[i] !=';':
            if (ord(s[i])<=122 and ord(s[i])>=97) or (ord(s[i])<=90 and ord(s[i])>=65):
                r = ord(s[i])
            else:
                fg = False
            i+=1
            enter = True
        if fg and enter:
            res += abs(l-r)
            # print(l,r)
        i+=1
    return res

print(f())
