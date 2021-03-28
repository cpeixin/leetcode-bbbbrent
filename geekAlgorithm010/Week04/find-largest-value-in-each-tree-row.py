# coding: utf-8
# Author：Brent
# Date ：2020/6/29 9:39 PM
# Tool ：PyCharm
# Describe ：您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# 输出: [1, 3, 9]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row


class Solution(object):
    """BFS"""

    def largestValues_BFS(self, root):
        if not root: return []
        res, queue = [], [root]
        while queue:
            max_num = float('-inf')
            for index in range(len(queue)):
                node = queue.pop(0)
                max_num = max(max_num, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                res.append(max_num)
        return res

    def largestValues_DFS(self, root):
        ans = []

        def help(root, level):
            if not root: return
            if len(ans) <= level:  # 遇到最新一层
                ans.append(float('-inf'))
            ans[level] = max(ans[level], root.val)
            help(root.left, level + 1)
            help(root.right, level + 1)

        help(root, 0)  # 初始化为0问题！
        return ans
