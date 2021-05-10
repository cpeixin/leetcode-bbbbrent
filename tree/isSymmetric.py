#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 8:15 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : isSymmetric.py
# @Description:给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        def recur(left, right):
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False
            return recur(left.left, right.right) and recur(left.right, right.left)

        return recur(root.left, root.right)


# 遍历
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        queue = [root.left, root.right]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            if not left and not right: continue
            if not left or not right or left.val != right.val: return False

            # 将左节点的左孩子， 右节点的右孩子放入队列
            queue.append(left.left)
            queue.append(right.right)
            # 将左节点的右孩子，右节点的左孩子放入队列
            queue.append(left.right)
            queue.append(right.left)

        return True