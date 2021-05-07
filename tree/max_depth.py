# coding: utf-8
# Author：Brent
# Date ：2020/9/28 3:43 PM
# Tool ：PyCharm
# Describe ：


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# 自底向上
class Solution:
    def maxDepth(self, root):
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


# 自顶向下
class Solution:
    def maxDepth(self, root):
        Solution.answer = 0

        def depth(root, d):
            if not root: return
            if not root.left and not root.right:
                Solution.answer = max(Solution.answer, d)
            depth(root.left, d + 1)
            depth(root.right, d + 1)

        depth(root, 1)
        return Solution.answer


# 层序遍历
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depth = 0
        queue = [root]
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
