# coding: utf-8
# Author：Brent
# Date ：2020/9/14 12:50 PM
# Tool ：PyCharm
# Describe ：中序遍历


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorder(self,root):
        res, stack = [], []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = root.right
        return res