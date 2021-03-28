# coding: utf-8
# Author：Brent
# Date ：2020/6/20 1:25 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树，检查它是否是镜像对称的。
#
#  
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root.left, root.right) if root else True
    def recur(self,left_node, right_node):
        if not left_node and not right_node: return True
        if not left_node or not right_node or left_node.val!=right_node.val: return False
        return self.recur(left_node.left, right_node.right) and self.recur(left_node.right, right_node.left)