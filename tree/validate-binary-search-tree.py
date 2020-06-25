# coding: utf-8
# Author：Brent
# Date ：2020/6/25 10:49 AM
# Tool ：PyCharm
# Describe ：给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        def recur(node, lower=float('-inf'), upper=float('inf')):
            if not node: return True
            if node.val <= lower or node.val >= upper: return False
            if not recur(node.left, lower, node.val): return False
            if not recur(node.right, node.val, upper): return False
            return True
        return recur(root)
