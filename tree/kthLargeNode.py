# coding: utf-8
# Author：Brent
# Date ：2020/10/6 4:15 PM
# Tool ：PyCharm
# Describe ：给定一棵二叉搜索树，请找出其中第k大的节点。
#
#  
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
import collections
import heapq


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return None
        queue =collections.deque([root])
        heap = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if len(heap) < k+1:
                    heapq.heappush(heap, -node.val)
                else:
                    heapq.heapreplace(heap, -node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return -heap[0]



if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    solution = Solution()
    res = solution.kthLargest(root, 3)

    print(res)