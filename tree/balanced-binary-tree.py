# coding: utf-8
# Author：Brent
# Date ：2020/6/28 8:20 AM
# Tool ：PyCharm
# Describe ：给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree


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