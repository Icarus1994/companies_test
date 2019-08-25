# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:39
# @Author : icarusyu
# @FileName: 2019_消消乐.py
# @Software: PyCharm
import itertools


def xxx(board):
    m, n = len(board), len(board[0])
    while True:
        delete = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    continue
                x0, x1, y0, y1 = i, i, j, j
                while x0 >= 0 and x0 > i - 3 and board[x0][j] == board[i][j]:
                    x0 -= 1
                while x1 < m and x1 < i + 3 and board[x1][j] == board[i][j]:
                    x1 += 1
                while y0 >= 0 and y0 > j - 3 and board[i][y0] == board[i][j]:
                    y0 -= 1
                while y1 < n and y1 < j + 3 and board[i][y1] == board[i][j]:
                    y1 += 1
                if x1 - x0 > 3 or y1 - y0 > 3:
                    delete.append((i, j))
        if len(delete) == 0:
            break
        for a in delete:
            board[a[0]][a[1]] = 0
        for j in range(n):
            t = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j]:
                    board[t][j], board[i][j] = board[i][j], board[t][j]
                    t -= 1
    result = set(list(itertools.chain(*board)))

    if 0 in result:
        return len(result) - 1
    return len(result)


l = [[3, 1, 2, 1, 1],
     [1, 1, 1, 1, 3],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [3, 1, 2, 2, 2]]
print(xxx(l))

# 消消乐参考的是leetcode 700多题目