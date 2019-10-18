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
    # 栈实现非递归先序遍历,复杂度O(n)
    # 思路
    # 遍历node时，打印-存起来-移动到左子节点
    def preorder(self,root):
        if not root:return
        stack = []
        node = root
        res = []
        # while的条件可以从下方node = node.right推测
        # 赋值后的node为空表示stack里pop出的节点右子节点已经为空了
        # stack里存的节点是已经遍历过其左子节点的根节点，留着他们是为了遍历其右子树
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    # 栈实现非递归中序遍历
    # 思路
    # 遍历node时，存起来-移动到左子节点，直到node为空（表示一个节点的左子树已经遍历完了），那么此时打印根节点
    def inorder(self,root):
        if not root:return
        stack =[]
        node = root
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    # 两个栈栈实现非递归后序遍历
    def afterorder(self,root):
        if not root:
            return
        stack1 = [root] # stack1存放的是按照根-左子树-右子树的顺序存放的节点
        stack2 = [] # stack2每次append的是根节点，存放的是后续遍历的逆序
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)
            # 后序遍历是左-右-根，按理应该先append右子节点，但这里为什么先append左子节点呢？
            # 因为这样会先遍历右子树，那么右子树里的节点存放在stack2里就会位于比左子树节点靠前的位置，最后stack2.reverse就是我们想要的顺序
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack2.append(node.right)
        stack2.reverse()
        return stack2




root = treeNode(1)
node2 = treeNode(2)
node3 = treeNode(3)
node4 = treeNode(4)
root.left = node2
root.right = node3
node2.right = node4
print(solution().f(root))

# 参考：https://blog.csdn.net/qq_34178562/article/details/79548750



