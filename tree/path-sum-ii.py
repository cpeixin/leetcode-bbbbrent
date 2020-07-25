# coding: utf-8
# Author：Brent
# Date ：2020/7/24 11:14 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-ii

# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def dfs(root, sum):
            if not root: return []
            path.append(root.val)
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                # 这里要注意，如果res.append(path), 每次path变化的时候，res中已添加的path也会改变
                # 浅拷贝的原因。所以加上list，创建一个新对象。
                res.append(list(path))
            dfs(root.left, sum)
            dfs(root.right, sum)
            path.pop()
        dfs(root, sum)
        return res


if __name__ == '__main__':
    case = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), right=None),TreeNode(8, TreeNode(13),TreeNode(4,right=TreeNode(1))))
    result = case.pathSum(root, 22)