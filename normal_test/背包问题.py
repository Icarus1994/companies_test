
# -*- coding: utf-8 -*-
# @Time : 2019-09-20 16:05
# @Author : icarusyu
# @FileName: 背包问题.py
# @Software: PyCharm
# 01背包问题
# 有一个容量为v的背包和n个物品，第i个物品的重量是wi,价格是pi,往背包里装物品，返回能装进背包的最多的价值
# 思路
# 开辟一个dp数组，dp[i][j]表示容量为j的背包，从0-i-1个物品中选取物品往背包里放时能得到的最大价值
# 状态转移方程：dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + p[i])
# 其中dp[i-1][j]表示对容量为j的书包，不往里面放物品i
# dp[i-1][j-w[i]] + p[i]表示往里面放物品i，而其价值计算方式为，
# 先将i从容量为j的书包中取出，找到容量为j-w[i]时对前i-1个物品能获得的最大价值（用到了之前的解，动态规划的核心）

# 内存优化
# 因为每次只用到上一行（i-1行）数组的数据（dp[i-1]），可以设置cur,next两个数组
# 更简洁地，可以只创建一个数组a，让v从大到小遍历。因为a[j]更新时只与i-1,j时和i-1,j-w[i]的背包价值有关，因此更新时
# 数组a中大于j的元素都是更新i时的价值，小于j的都是i-1时的价值
# 参考：https://blog.csdn.net/wzy_1988/article/details/12260343

# 完全背包问题
# 与01背包的区别是，每种物品有无限多个，可选0-多个
