# coding: utf-8
# Author：Brent
# Date ：2020/9/11 1:48 AM
# Tool ：PyCharm
# Describe ：给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
#
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-width-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 1
        queue = [root]
        idx = [1]
        while queue:
            l = len(queue)
            ans = max(ans,idx[-1]- idx[0] + 1)
            for i in range(l):
                node = queue.pop(0)
                index = idx.pop(0)
                if node.left:
                    queue.append(node.left)
                    idx.append(2*index)
                if node.right:
                    queue.append(node.right)
                    idx.append(2*index + 1)
        return ans
