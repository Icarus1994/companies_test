# -*- coding: utf-8 -*-
# @Time : 2019-10-17 17:01
# @Author : icarusyu
# @FileName: topk.py
# @Software: PyCharm

# top k问题
# 经典解法：用堆，求前k个最大元素，则构造k个元素的最小堆，遍历数组时与最小堆堆顶元素比较
# O(nlogk)

# bfprt算法 只能用于求第k大的数时时间复杂度是线性的
# T(n) <= T(n/5) + T(n*7/10) + O(n)
# 参考：https://todebug.com/BFPRT/
# https://blog.csdn.net/qq_26437925/article/details/53809495