#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 8:05 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : levelOrder.py
# @Description:给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#  
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefh1i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        res, queue = [], [root]
        while queue:
            tmp = []
            for i in range(len(queue)):
                current = queue.pop(0)
                tmp.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            res.append(tmp)
        return res


if __name__ == '__main__':
    tree_3 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                      TreeNode(1, TreeNode(0), TreeNode(8)))
    result = Solution.levelOrder(tree_3)
    print(result)
