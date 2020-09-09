# coding: utf-8
# Author：Brent
# Date ：2020/9/9 5:19 PM
# Tool ：PyCharm
# Describe ：给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Soulution:
    """递归方法"""
    def preorder(self, root):
        res = []
        self.helper(root, res)
        return res


    def helper(self, root, res):
        if not root: return None
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)


    """BFS
    如果使用广度优先遍历，需要注意的是"先入后出"的关键
    对于前序遍历，中->左->右的这个顺序
    需要在栈中先添加右孩子，再添加左孩子，这样在pop()的顺序就是先弹出左孩子，再弹出右孩子
    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res