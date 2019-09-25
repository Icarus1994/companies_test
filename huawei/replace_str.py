# -*- coding: utf-8 -*-
# @Time : 2019-09-25 19:11
# @Author : icarusyu
# @FileName: replace_str.py.py
# @Software: PyCharm
def f():
    raw, m = input().split()
    i = 0
    while i < len(raw):
        if raw[i] == m[0]:
            j = 0
            fg = True
            while j < len(m):
                if raw[i+j] == m[j]:
                    j+=1
                else:
                    fg = False
                    break
            # print('j',j)
            # print('i',i)
            # print('raw',raw[:i]+'***')
            if fg:
                s = ''
                for k in range(len(m)):
                    s += '*'
                return raw[:i] + s + raw[i+len(m):]
        i +=1
    return raw
print(f())
