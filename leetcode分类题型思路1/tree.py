# -*- coding: utf-8 -*-
# @Time : 2019-10-18 16:44
# @Author : icarusyu
# @FileName: tree.py
# @Software: PyCharm
'''

98. Validate Binary Search Tree
方法一
思路：递归，当一个节点所在树满足bst要求时（即节点值属于某个区间），要判断其儿子节点是否满足要求，只要满足更新后的区间即可
例如：一开始根节点满足[-inf,inf]即可，验证过根节点满足bst要求后，递归进入左子节点，判断属于(root.val,inf)
右子节点是否满足(-inf,root.val)，返回左右儿子节点取and的结果

原理是：当树包含了当前节点时是bst时，当前节点满足一个取值区间，那么其儿子节点值当且仅当满足更新的区间
那么树加入这个儿子节点也是满足bst条件的

方法二：
思路：bst中序遍历时非递减的数组，一边遍历一边比较是否大于前一个值
'''