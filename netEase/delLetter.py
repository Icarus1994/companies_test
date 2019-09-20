# -*- coding: utf-8 -*-
# @Time : 2019-09-20 18:03
# @Author : icarusyu
# @FileName: delLetter.py
# @Software: PyCharm
def f():
    k,s = input().split(',')
    k = int(k)
    if k >= len(s):
        return 0
    while k >0:
        i = 0
        while i < len(s):
            if s[i] == '0':
                break
            i+=1
        if k >= i:
            j = i
            while j < len(s):
                if s[j] != '0':
                    break
                j +=1
            s = s[j:]
            # print('s1',s)
            k -= i
            if s == '':return 0
        else:
            fg = False
            for m in range(len(s)-1):
                if s[m] > s[m+1]:
                    fg = True
                    break
            if fg:
                s = s[:m] + s[m+1:]
            else:
                s = s[:-1]
            # print('s',s)
            k -= 1
            if s == '':return 0
    return int(s)
print(f())