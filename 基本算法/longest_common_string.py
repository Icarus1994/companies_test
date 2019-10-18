# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:57
# @Author : icarusyu
# @FileName: longest_common_string.py
# @Software: PyCharm
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        max_v = 0
        for i in range(len(B)):
            for j in range(len(A)):
                if B[i] == A[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_v = dp[i][j] if dp[i][j] > max_v else max_v
        return max_v
# 最长公共子串问题
# 动态数组dp[i][j]表示以A[j],B[j]结尾的A[:j+1],B[:i+1]数组的公共子串长度
