# coding: utf-8
# Author：Brent
# Date ：2020/6/25 4:39 PM
# Tool ：PyCharm
# Describe ：根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return
        root  = TreeNode(postorder[-1])
        in_root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:in_root_index], postorder[:in_root_index])
        root.right = self.buildTree(inorder[in_root_index+1:], postorder[in_root_index:-1])
        return root