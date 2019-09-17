# -*- coding: utf-8 -*-
# @Time : 2019-09-16 21:55
# @Author : icarusyu
# @FileName: shudu.py
# @Software: PyCharm
def f():
    arr = []
    for i in range(9):
        arr.append(input())
    fg = True
    row = [{''} for i in range(9)]
    col = [{''} for i in range(9)]
    rec = {'00':[],'01':[],'02':[],
           '10':[],'11':[],'12':[],
           '20':[],'21':[],'22':[]
           }
    # fg = True
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 'X':
                continue
            if arr[i][j] not in row[i]:
                row[i].add(arr[i][j])
            else:
                print('false')
                return
                # return False
            if arr[i][j] not in col[j]:
                col[j].add(arr[i][j])
            else:
                print('false')
                return
                # return False
            if arr[i][j] not in rec[str(i//3) + str(j//3)]:
                # print(i//3,j//3)
                rec[str(i//3) + str(j//3)].append(arr[i][j])
            else:
                print('false')
                return
                # return False
    # return True
    print('true')



f()
# print(f())