# coding: utf-8
# Author：Brent
# Date ：2020/6/21 12:18 PM
# Tool ：PyCharm
# Describe ：
class TreeNode:
    def __init__(self, x, left_child_node=None, right_child_node=None):
        self.val = x
        self.left = left_child_node
        self.right = right_child_node

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left and not right: return  # 1.
    if not left: return right  # 3.
    if not right: return left  # 4.
    return root  # 2. if left and right:

if __name__ == '__main__':
    tree_3 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    result = lowestCommonAncestor(tree_3, TreeNode(7), TreeNode(4))
    print(result)
