# -*- coding: utf-8 -*-
# @Time : 2019-09-27 11:52
# @Author : icarusyu
# @FileName: 二叉树遍历_全.py
# @Software: PyCharm
class treeNode:
    def __init__(self,val = None):
        self.val = val
        self.left =None
        self.right = None

class solution:
    # 非递归先序遍历,复杂度O(n)
    def f(self,root):
        if not root:return
        heap = [root]
        res  =[]
        while len(heap)>0:
            node = heap.pop()
            res.append(node.val)
            if node.right:
                heap.append(node.right)
            if node.left:
                heap.append(node.left)
        return res
root = treeNode(1)
node2 = treeNode(2)
node3 = treeNode(3)
node4 = treeNode(4)
root.left = node2
root.right = node3
node2.right = node4
print(solution().f(root))



