# coding: utf-8
# Author：Brent
# Date ：2020/8/19 2:05 PM
# Tool ：PyCharm
# Describe ：
import collections


class TreeNode:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):

        if not root: return []
        queue = collections.deque()
        queue.append(root)

        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                if len(res) % 2 != 0:
                    node = queue.popleft()
                    tmp.append(node.val)
                else:
                    node = queue.pop()
                    tmp.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)



