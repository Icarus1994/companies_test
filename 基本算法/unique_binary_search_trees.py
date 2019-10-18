# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:52
# @Author : icarusyu
# @FileName: unique_binary_search_trees.py
# @Software: PyCharm

# 参考：https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/
# Python3 prgroam to contrcut all unique
# BSTs for keys from 1 to n

# Binary Tree Node
""" A utility function to create a
new BST node """


class newNode:

    # Construct to create a newNode
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None


# A utility function to do preorder
# traversal of BST
def preorder(root):
    if (root != None):
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

    # function for constructing trees


def constructTrees(start, end):
    list = []

    """ if start > end then subtree will be 
        empty so returning None in the list """
    if (start > end):
        list.append(None)
        return list

    """ iterating through all values from 
        start to end for constructing 
        left and right subtree recursively """
    for i in range(start, end + 1):

        """ constructing left subtree """
        leftSubtree = constructTrees(start, i - 1)

        """ constructing right subtree """
        rightSubtree = constructTrees(i + 1, end)

        """ now looping through all left and 
            right subtrees and connecting 
            them to ith root below """
        for j in range(len(leftSubtree)):
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = newNode(i)  # making value i as root
                node.left = left  # connect left subtree
                node.right = right  # connect right subtree
                list.append(node)  # add this tree to list
    return list


# Driver Code
if __name__ == '__main__':

    # Construct all possible BSTs
    totalTreesFrom1toN = constructTrees(1, 3)

    """ Printing preorder traversal of 
        all constructed BSTs """
    print("Preorder traversals of all",
          "constructed BSTs are")
    for i in range(len(totalTreesFrom1toN)):
        preorder(totalTreesFrom1toN[i])
        print()

    # This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)

# 思路
# 要构成一棵树，则将其中每个元素作为根节点，求其左子树left和右子树right，将node.left = left这种方式将根节点与左子树和右子树连起来。每个left，right都是通过node.left,node.right的方式构建好的树
# 题目中list装的是某个节点为根节点时所有左子树（右子树）的根节点。从整体上看，对于start,end中的每个根节点，求所有左/右子树构成的list,分别与左右子树连接构成所有的树。
# 而求左子树和右子树也是将其作为一颗树递归地求。
