# coding: utf-8
# Author：Brent
# Date ：2020/7/11 10:39 PM
# Tool ：PyCharm
# Describe ：给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :
# 返回其前序遍历: [1,3,5,6,2,4]。

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    """递归实现"""

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        res = []

        def recur(root):
            res.append(root.val)
            for child in root.children:
                recur(child)

        recur(root)
        return res

    def preorder_iteration(self, root):
        if not root: return []
        res, queue = [], [root]
        while queue:
            node = queue.pop()
            # 前序遍历，添加值到结果中
            res.append(node.val)
            # [::1]
            for child in node.children[::-1]:
                queue.append(child)
        return res
