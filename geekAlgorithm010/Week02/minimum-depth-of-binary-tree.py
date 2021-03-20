# coding: utf-8
# Author：Brent
# Date ：2020/6/16 5:58 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        if not root.left or not root.right:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1