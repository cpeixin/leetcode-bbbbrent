# coding: utf-8
# Author：Brent
# Date ：2020/8/7 10:12 PM
# Tool ：PyCharm
# Describe ：给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
#
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/same-tree

class Solution(object):
    def isSameTree(self, p, q):
        if p.val != q.val: return False
        if not p and not q: return True
        if not p or not q: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)