# -*- coding: utf-8 -*-
# @Time : 2019-10-26 14:24
# @Author : icarusyu
# @FileName: 头条面试算法题.py
# @Software: PyCharm
'''
23 成对链表的反转
设置pre,node,tmp三个指针，循环条件为while node and node.next即可



【拓扑排序】
207
210 拓扑排序2
题目：给定每两个课程的先修关系，所有先修关系构成一个图
如果是DAG,要求返回符合先修关系的所有课程构成的上课顺序，如果有环则返回[]

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # if numCourses == 2 and len(prerequisites) ==0 :return [1,0]
        # if numCourses ==1:return [0]
        visited = [0] * numCourses
        after = collections.defaultdict(list)
        res = []
        for u,v in prerequisites:
            after[u].append(v)

        def dfs(visited,after,node):
            if visited[node]==1:return False
            if visited[node]==2:return True
            visited[node]=1

            for i in after[node]:
                if dfs(visited,after,i) == False:
                    return False # 一步步把false的结果传递到最开始进行bfs的节点
            res.append(node)
            visited[node]=2
            return True
        for i in range(numCourses): # 对每个节点都访问一次，判断从该节点出发寻找它的先修课程
            if dfs(visited, after,i) == False:
                return []
        return res


dfs, O(n)
visited=1表示正在访问该节点，还没访问完，2表示已经访问完，0表示还未访问
和lc 207相反，after里的v是所有指向k节点的节点，所以第27行可以从任一节点出发，一直寻找先修课程，直到找到不需要先修的课程并访问（visited[i]=2,res.append）或者发现有冲突（visited[i]==1）为止。
因为调用dfs找的是节点的先修课程，并且使用dfs，所以直接对res使用append方法可以将节点放到正确位置上
dfs拓扑排序
参考：https://www.runoob.com/python3/python-topological-sorting.html



蓄水池算法
问题抽象：
有一组未知大小的数组（假设长度为n），要从数组中等概率地抽取k个数
算法过程：
对于数组前k个数，直接放入大小为k的数组a中
对于第j个数（j>k）,以【k/j】的概率放入数组a中，如果放入，则剔除a中一个元素（a中每个元素有相等概率即1/k被剔除）
实现：
概率方面都用randint实现，k/j的概率放入数组，则在(1,j)之间随机取整数，当整数>k则不替换原数组a的元素
对于数组a中元素的等概率替换，随机选取(1,k)中的整数，替换该坐标对应的元素
证明过程：
分为对前k个数，证明被留下的概率是k/n;对于后面的数，证明也是有k/n的概率被留下来：k/j * (j/j+1)*...(n-1/n)-k/n
参考：https://blog.csdn.net/anshuai_aw1/article/details/88750673

382. Linked List Random Node
题目：给一个链表的表头，返回链表值中随机的一个值，这题是k=1的特殊情况，当数组a中元素要被替换时，
则其中元素被100%的概率替换


k means
算法原理：
1、随机选取k个样本作为初始均值向量 random.randint(a,b) # 包括a,b，设置列表lst存放各质心
2、更新各样本所在簇
设置一个元素为list的列表lst2,lst2中第i个元素表示第i个簇包含的样本
遍历样本
    遍历k个质心
        设置min_v和idx,计算样本到质心的距离更新min_v,idx，样本min_v插入到lst2第i个元素（list）的末尾
        距离的计算可以用c = [pow(a[i] - b[i],2) for i in range(len(a)) ],sum(c)得到
3、更新质心（簇中各向量均值）
4、当3中更新的各质心和原来的完全一样，或者达到了循环次数，结束循环否则继续2，3

参考：https://blog.csdn.net/abc13526222160/article/details/96482592#pythonkmeans_20
https://blog.csdn.net/louishao/article/details/76619159


209 求和大于k的子串的最小长度
双指针O(n)
前缀和+二分查找O(nlogn)

两个01数组，找到对应位置的最长子数组使其拥有相同个数的1
思路：
双指针，当l<r时循环
    判断arr[l:r+1]是否满足条件
    不满足则当a[l]+b[l]==1时l一直向右移动
    当a[r]+b[r]==1时一直向做移动


 给几个二维坐标，坐标的连线间都是垂直的，并且最终形成闭环，求连线的k等分点坐标
思路：
先按照简单的来，找到最上，最下，最左，最右的点构成闭环，求等分时的长度
从第一个点开始，找点1到点2时候


买卖股票1次(分治，得到排序的左右子数组，右[-1]-左[0])，多次(双指针)，买股票hard(lc123) 问过多遍

编辑距离，带权编辑距离问多次

二叉树最近公共祖先：递归

数组中出现次数大于数组长度一半的数字
思路：湮灭
如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多，将这个数字与其他数字相互湮灭
在遍历数组时保存两个值：一是数组中一个数字，一是次数。
遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；
若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。
然后再判断它是否符合条件即可。遍历判断出现次数
'''
