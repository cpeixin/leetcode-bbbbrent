# coding: utf-8
# Author：Brent
# Date ：2020/9/26 8:16 AM
# Tool ：PyCharm
# Describe ：
class TreeNode:
    def __init__(self,value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode):
        ans=[]
        most=0
        last=None
        cnt=0

        def inorder(node):
            if not node: return
            nonlocal ans,most,last,cnt
            if node.left: inorder(node.left)
            if node.val==last:
                cnt+=1
            else: cnt=1
            if cnt==most: ans.append(node.val)
            elif cnt>most:
                most=cnt
                ans=[node.val]
            last=node.val
            if node.right: inorder(node.right)

        inorder(root)
        return ans


if __name__ == '__main__':
    tree_3 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    result = Solution.findMode(tree_3)
    print(result)