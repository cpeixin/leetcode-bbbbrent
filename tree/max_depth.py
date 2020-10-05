# coding: utf-8
# Author：Brent
# Date ：2020/9/28 3:43 PM
# Tool ：PyCharm
# Describe ：




class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right) + 1


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))