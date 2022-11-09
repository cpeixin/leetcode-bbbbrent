#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/10 6:24 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : increasingBST.py
# @Description:
# 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，
# 并且每个节点没有左子节点，只有一个右子节点。https://leetcode.cn/problems/NYBBNL/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """