# coding: utf-8
# Author：Brent
# Date ：2020/9/1 12:13 AM
# Tool ：PyCharm
# Describe ：

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root):
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right) + 1