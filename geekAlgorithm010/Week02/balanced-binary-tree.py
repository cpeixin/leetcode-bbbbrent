# coding: utf-8
# Author：Brent
# Date ：2020/6/19 2:36 PM
# Tool ：PyCharm
# Describe ：

class TreeNode:
    def __init__(self, x, left_child_node=None, right_child_node=None):
        self.val = x
        self.left = left_child_node
        self.right = right_child_node


def isBalanced(root: TreeNode) -> bool:
    return recur(root) != -1


def recur(root):
    if not root: return 0
    left = recur(root.left)
    if left == -1: return -1
    right = recur(root.right)
    if right == -1: return -1
    return max(left, right) + 1 if abs(left - right) < 2 else -1


if __name__ == '__main__':
    tree_3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    result = isBalanced(tree_3)
    print(result)