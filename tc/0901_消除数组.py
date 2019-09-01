# -*- coding: utf-8 -*-
# @Time : 2019-09-01 19:52
# @Author : icarusyu
# @FileName: 0901_消除数组.py.py
# @Software: PyCharm
import sys
class solution:
    # 解法1 ac 0%
    def f(self):
        group = int(sys.stdin.readline())
        ans = []
        while group >0:
            n = int(sys.stdin.readline())
            arr = sys.stdin.readline().split()
            arr.sort()
            i = 0
            cnt = 0
            remain = len(arr)
            while i < len(arr)-1:
                if arr[i] == arr[i+1]:
                    v = arr[i]
                    l = i
                    while i<len(arr) and arr[i] == v:
                        i +=1
                    cnt = abs(cnt-i+l)
                    remain -= i-l
                else: i+=1
            if remain >= cnt:
                # print('YES')
                ans.append('YES')
            else:
                # print('NO')
                ans.append('NO')
            group -= 1
        for i in range(len(ans)):
            print(ans[i])

solution().f()

if __name__== "__main__":
    # 解法2 ac
    T = int(input())
    while T>0:
        T -=1
        n = int(input())
        nums = list(map(int,input().split()))
        Dict = {}
        unique_num = 0
        anti_unique_num = 0
        max_appear_num = 0
        for ele in nums:
            if ele not in Dict:
                Dict[ele] = 1
                unique_num += 1
            else:
                Dict[ele] += 1
                anti_unique_num += 1
                max_appear_num = max(max_appear_num,Dict[ele])
        if unique_num >= anti_unique_num:
            print("YES")
        elif max_appear_num > int(n/2):
            print("NO")
        else:
            print("YES")

# 题目
# 偶数个元素的数组，每次取两个不同的数则可以将这两个数从数组中删除，求数组所有元素是否能被完全消除