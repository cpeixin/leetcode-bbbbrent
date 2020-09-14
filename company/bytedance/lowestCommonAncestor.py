# coding: utf-8
# Author：Brent
# Date ：2020/8/19 11:02 AM
# Tool ：PyCharm
# Describe ：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class lowestCommonAncestor:
    def lowestCommonParent(self,root, p, q):
        if not root or p == root or q == root: return root
        left = self.lowestCommonParent(root.left, p, q)
        right = self.lowestCommonParent(root.right, p, q)

        if not left: return right
        if not right: return left

        if left and right: return root

