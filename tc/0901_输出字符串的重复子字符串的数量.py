# -*- coding: utf-8 -*-
# @Time : 2019-09-01 21:27
# @Author : icarusyu
# @FileName: 0901_输出字符串的重复子字符串的数量.py
# @Software: PyCharm
def f():
    limit = int(input())
    output = input().strip()
    output = output[:limit]
    m = int(input())
    cnt = 0
    for i in range(m):
        line = input().strip()
        # store.append(line)
        if len(line) >= limit:
            if line[:limit] == output:cnt +=1
        else:
            if line != output[:len(line)]:continue
            bei = limit//len(line) + 1
            t = ''
            for i in range(bei):
                t += line
            if t[:limit] == output:cnt+=1
    return cnt
print(f())

# 问题
# 给出指定长度字符串，问该子串最多有可能是以下子串重复得到？过长则截取超出长度的

# 结果
# case:70%，暴力求解