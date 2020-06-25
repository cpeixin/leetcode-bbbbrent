# coding: utf-8
# Author：Brent
# Date ：2020/6/25 9:53 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        sum -= root.val
        if not root.left and not root.right: return sum == 0
        # 先执行左子树，如果左子树不符合，则执行 or self.hasPathSum(root.right, sum)
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

if __name__ == '__main__':
    case = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), right=None),TreeNode(8, TreeNode(13),TreeNode(4,right=TreeNode(1))))
    result = case.hasPathSum(root, 22)