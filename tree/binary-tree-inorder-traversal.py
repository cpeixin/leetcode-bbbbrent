# coding: utf-8
# Author：Brent
# Date ：2020/9/9 6:54 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        res = []
        self.helper(root, res)
        return res


    def helper(self, root, res):
        if not root: return None
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    """BFS"""
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        curr_node, stack = root, []
        while curr_node or stack:
            """当curr_node还有左孩子"""
            while curr_node:
                """中序遍历：左  中  右
                最先打印左子树  左叶子节点，所以，最后添加左叶子节点
                """
                stack.append(curr_node)
                curr_node = curr_node.left
            """左子树遍历完毕后"""
            curr_node = stack.pop()
            res.append(curr_node.val)
            """叶子节点的话，curr_node.right为空"""
            curr_node = curr_node.right
        return res