# -*- coding: utf-8 -*-
# @Time : 2019-09-03 16:12
# @Author : icarusyu
# @FileName: 0902_合并区间.py
# @Software: PyCharm

# 问题（京东面试题）
# 给一个list,list里每个元素是装有一个区间的tuple,tuple中都是整数值
# 如果两个区间有交集，则可以合并两个区间。返回合并区间后的list

# 思路
# 将数组中元素按照tuple的第一个元素从小到大排序，判断是否能合并，返回最后结果
# 复杂度O(nlogn)