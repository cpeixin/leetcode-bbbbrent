# coding: utf-8
# Author：Brent
# Date ：2020/6/25 5:38 PM
# Tool ：PyCharm
# Describe ：从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#
#  
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：
#
# [3,9,20,15,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof

class Solution:
    def levelOrder(self,root):
        if not root: return []
        res, queue = [], [root]
        while queue:
            node = queue.pop()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res