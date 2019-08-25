# -*- coding: utf-8 -*-
# @Time : 2019-07-28 14:47
# @Author : icarusyu
# @FileName: pdd.py
# @Software: PyCharm
# import sys
# for line in sys.stdin:
#     a = line.split()
class solution:
    def array(self,A,B):
        if not A:
            return "NO"
        if len(A)==1:
            return A
        for i in range(len(A)-1):
            if A[i]>=A[i+1]:
                break
        if not B:
            return "NO"
        max = A[i]
        fg = False
        for j in range(len(B)):
            if B[j]>A[i]:
                if i+2 < len(A):
                    if B[j]<A[i+2] and B[j]>max:
                        fg=True
                        A[i+1] = B[j]
                        max = B[j]
                elif B[j]>max:
                    fg=True
                    A[i+1] = B[j]
                    max = B[j]
        # 换掉前面的数
        max=-10000000
        if not fg:
            for j in range(len(B)):
                if i>0:
                    if B[j]>A[i-1] and B[j]<A[i+1] and B[j] > max: # 隐含了A[i-1]<A[i+1]时才能将B[j]替换为A[i]
                        fg = True
                        A[i] = B[j]
                elif B[j]<A[i+1] and B[j] > max:
                    fg=True
                    A[i] = B[j]
        return A if fg else "NO"
import sys
for i in range(2):
    if i == 0:
        line = sys.stdin.readline()
        A = list(map(float,line.split()))
    else:
        line = sys.stdin.readline()
        B = list(map(float,line.split()))
print(solution().array(A,B))

# for line in sys.stdin:
#     B = line.split()
# for i in A:
#     A[i] = float(A[i])
# for i in B:
#     B[i] = float(B[i])


# A = [1,3,7,4,10]
# B=[2,1,5,8,9]
# c=[20,1,23]
# d=[50,26,7]
# for i in range(2):
#     line = sys.stdin.readlines().strip()
#     print(line)


# for line in sys.stdin:
#     a = line.split()
#     print(a)
# for line in sys.stdin:
#     b  = line.split()
#     print(b)
