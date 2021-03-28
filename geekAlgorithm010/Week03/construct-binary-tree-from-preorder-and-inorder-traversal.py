# coding: utf-8
# Author：Brent
# Date ：2020/6/24 10:27 PM
# Tool ：PyCharm
# Describe ：根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        in_root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:in_root_index+1], inorder[:in_root_index])
        root.right = self.buildTree(preorder[in_root_index+1:], inorder[in_root_index+1:])
        return root