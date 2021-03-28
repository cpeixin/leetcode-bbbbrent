# coding: utf-8
# Author：Brent
# Date ：2020/6/30 8:44 PM
# Tool ：PyCharm
# Describe ：
from typing import List


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

if __name__ == '__main__':
    case = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), right=None),TreeNode(8, TreeNode(13),TreeNode(4,TreeNode(5),TreeNode(1))))
    result = case.pathSum(root, 22)
    print(result)