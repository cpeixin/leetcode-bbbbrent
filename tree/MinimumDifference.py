# coding: utf-8
# Author：Brent
# Date ：2020/10/12 9:21 PM
# Tool ：PyCharm
# Describe ：给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。


class Solution(object):
    pre, min_num = float('inf'), float('inf')
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def posOrder(root):
            if not root: return None
            posOrder(root.left)
            self.min_num = min(self.min_num, abs(self.pre - root.val))
            self.pre = root.val
            posOrder(root.right)
        posOrder(root)
        return self.min_num