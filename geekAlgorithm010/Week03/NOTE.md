# 算法10期_week_03

<a name="g32j4"></a>
### 大纲
递归/回溯/分治<br />

<a name="zstIN"></a>
### 解题思路
<a name="6cCQO"></a>
#### [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
递归，谜之递归
```python
class Solution:
	def generateParenthesis(n):
    	def generate(str, left, right, array=[]):
        	if left: generate(str+'(', left-1, right)
        	if right>left: generate(str+')', left, right-1)
        	if not right: array+=str,
        	return array
    	return generate('', n, n)
```


<a name="mPROv"></a>
#### [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)
可以使用递归左右子树，也可以利用中序遍历特性。<br />**<br />**递归左右子树**<br />这启示我们设计一个递归函数 helper(root, lower, upper) 来递归判断，函数表示考虑以 root 为根的子树，判断子树中所有节点的值是否都在 (l,r) 的范围内（注意是开区间）。如果 root 节点的值 val 不在 (l,r) 的范围内说明不满足条件直接返回，否则我们要继续递归调用检查它的左右子树是否满足，如果都满足才说明这是一棵二叉搜索树。<br />
<br />那么根据二叉搜索树的性质，在递归调用左子树时，我们需要把上界 upper 改为 root.val，即调用 helper(root.left, lower, root.val)，因为左子树里所有节点的值均小于它的根节点的值。同理递归调用右子树时，我们需要把下界 lower 改为 root.val，即调用 helper(root.right, root.val, upper)。
```python
class Solution:
    def isValidBST(self, root):
         def recur(node, lower = float(-inf), upper = float(inf)):
                if not node: return True
                value = node.val
                if value <= lower or value >= upper: return False
                if not recur(node.left, lower, value): return False
                if not recur(node.right, value, upper): return False
                return True
         return recur(root)
```
复杂度分析<br />**时间复杂度** : O(n)，其中 n 为二叉树的节点个数。在递归调用的时候二叉树的每个节点最多被访问一次，因此时间复杂度为 O(n)。<br />**空间复杂度** : O(n)，其中 n 为二叉树的节点个数。递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，即二叉树的高度。最坏情况下二叉树为一条链，树的高度为 n ，递归最深达到 n 层，故最坏情况下空间复杂度为 O(n) 。<br />

<a name="bGsqs"></a>
#### [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
划分为子问题就是，子节点到父节点的深度为 子节点+1
```python
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right)+1
```

<br />**复杂度分析**<br />**时间复杂度**：我们每个结点只访问一次，因此时间复杂度为 O(N)，其中 N是结点的数量。<br />**空间复杂度**：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。但在最好的情况下（树是完全平衡的），树的高度将是 log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))。<br />

<a name="erE1D"></a>
#### [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)
我的理解是，序列化的过程就是 二叉树遍历到数组的过程。反序列化则是数组返回到二叉树的过程
```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else: vals.append('#')
        doit(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(' '))
        def doit():
            val = next(vals)
            if val == '#': return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        return doit()
        
```


<a name="jlD3z"></a>
#### [从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
清晰明了的递归，借用优秀题解的话：
> 通过先序遍历我们可以找到root，根据root我们可以再中序找到当前root对应的左右子树，再递归对当前root的左右子树进行构造(递归的时候别想多，把看到的一堆想成一个整体就好,想好递归终止条件，剩下的让程序去做吧，不然容易把自己陷入死循环弄得一头雾水)。
> 本题也是一样，知道inorder中，当前root的左侧的所有点就是其左子树，root的右侧的所有点就是当前root的右子树，就把这左右两堆数字想成当前root的左右2个节点就好，然后扔到函数里进行下一层的递归。
> 直接看代码比较清楚些。

buildTree（）函数的两个参数分别是前序遍历数组，中序遍历数组。递归的时候，把左子树的前序遍历数组，中序遍历数组放入 buildTree（），把右子树的前序遍历数组，中序遍历数组放入 buildTree（）。
```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: return 
        # 前序遍历的第一个节点就是根节点
        # 中序遍历中根节点左右两边为左右子树
        root = TreeNode(preorder[0])
        in_root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:in_root_index+1], inorder[:in_root_index])
        root.right = self.buildTree(preorder[in_root_index+1:], inorder[in_root_index+1:])
        return root
```
复杂度分析：<br />时间复杂度：O(n^2)<br />空间复杂度：O(n)<br />这里注意一下，虽然一般的二叉树递归，时间复杂度都是O(n)的，但是上面程序中使用了index()，这个内置方法的时间复杂度是n^2的，因为使用了复杂性的朴素算法`O(n^2)`<br />

<a name="T3819"></a>
#### [从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
和上一题一样。主要是先序，中序，后序数组的边界容易出错。
```python
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return 
        root  = TreeNode(postorder[-1])
        in_root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:in_root_index], postorder[:in_root_index])
        root.right = self.buildTree(inorder[in_root_index+1:], postorder[in_root_index:-1])
        return root
```
复杂度分析：<br />时间复杂度：O(n^2)<br />空间复杂度：O(n)<br />

<a name="hl1TM"></a>
#### [组合](https://leetcode-cn.com/problems/combinations/)
**给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。**<br />**输入: n = 4, k = 2**<br />**输出:[[2,4],[3,4],[2,3],。。。。。]**<br />
<br />没啥可说的，排列组合题，又是循环又是递归的，看起来挺难懂的，但是把下面三道题都手抄一遍，会发现一些套路的！！！！！
```python
def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = list()
        def solve(m, k, item_list):
            if k==0: result.append(item_list)
            else:
                for i in range(m+1, n+1):
                    solve(i, k-1, item_list+[i])
        solve(0, k, [])
        return result
```
![截屏2020-06-26 下午9.48.59.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593179372120-bd7f67ac-7f28-4764-af7b-7de581512809.png#align=left&display=inline&height=402&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-26%20%E4%B8%8B%E5%8D%889.48.59.png&originHeight=402&originWidth=1536&size=78170&status=done&style=none&width=1536)<br />

<a name="j9ECN"></a>
#### [全排列](https://leetcode-cn.com/problems/permutations/)
给定一个** 没有重复** 数字的序列，返回其所有可能的全排列。<br />**示例:输入:** [1,2,3]<br />
<br />没啥可说的，排列组合题，又是循环又是递归的，看起来挺难懂的，但是把下面三道题都手抄一遍，会发现一些套路的！！！！！
```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def back_track(nums, tmp):
            if not nums: res.append(tmp)
            else:
                for i in range(len(nums)):
                    back_track(nums[:i]+nums[i+1:], tmp+[nums[i]])
        back_track(nums, [])
        return res
```
![截屏2020-06-26 下午9.53.30.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593179666113-a1545193-4dca-4782-9961-b93d571964c2.png#align=left&display=inline&height=742&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-26%20%E4%B8%8B%E5%8D%889.53.30.png&originHeight=742&originWidth=1606&size=200839&status=done&style=none&width=1606)
<a name="8Snqc"></a>
#### [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)
给定一个可包含重复数字的序列，返回所有不重复的全排列。**示例:输入:** [1,1,2]

没啥可说的，排列组合题，又是循环又是递归的，看起来挺难懂的，但是把下面三道题都手抄一遍，会发现一些套路的！！！！！
```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(nums, tmp_list, lengh):
            if lengh == n and tmp_list not in res:
                res.append(tmp_list)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:], tmp_list+[nums[i]], lengh+1)
        backtrack(nums, [], 0)
        return res
"""简洁版本，和全排列仅一处不同"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def backtrack(nums, tmp_list):
            if not nums and tmp_list not in res:
                res.append(tmp_list)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:], tmp_list+[nums[i]])
        backtrack(nums, [])
        return res
```

- 时间复杂度：_O_(_N_×_N_)，这里 N为数组的长度。
- 空间复杂度：_O_(_N_×_N_)。

[https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/)

<a name="prEoj"></a>
#### [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)
没咋理解这道题，答案先写上吧。
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
```
复杂度分析<br />时间复杂度：O(logn)，即为递归的层数。<br />空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。<br />

<a name="VP5Gb"></a>
#### [子集](https://leetcode-cn.com/problems/subsets/)
输入: nums = [1,2,3] 输出:<br />[<br /> [3],[1],[2],[1,2,3],[1,3], [2,3], [1,2], []<br />]
```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        res = []
        n = len(nums)
        def backtrack(first, temp_list):
            res.append(temp_list)
            for i in range(first, n):
                backtrack(i+1, temp_list+[nums[i]])
        backtrack(0, [])
        return res
```
<a name="nVQIn"></a>
#### ![截屏2020-06-27 上午9.10.04.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593220736114-2cc74a49-2113-4f97-aabe-db12ac1ef6d5.png#align=left&display=inline&height=248&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-27%20%E4%B8%8A%E5%8D%889.10.04.png&originHeight=248&originWidth=1516&size=51504&status=done&style=none&width=1516)
<a name="fgziB"></a>
#### [子集 II](https://leetcode-cn.com/problems/subsets-ii/)
输入: [1,2,2]<br />输出:[[2], [1],[1,2,2],[2,2],[1,2],[]]
```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(first, tmp_list):
            if tmp_list not in res: res.append(tmp_list)
            for i in range(first, n):
                backtrack(i+1, tmp_list+[nums[i]])
        backtrack(0, [])
        return res

```
<a name="uFJiQ"></a>
#### 
<a name="wdFtc"></a>
#### [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
```python
def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_ = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []
        
        def make_combinations(i, cur):
            if i == len(digits):
                if len(cur) > 0:
                    result.append(''.join(cur))
                return
            for ch in map_[digits[i]]:
                cur.append(ch)
                make_combinations(i+1, cur)
                cur.pop()
        
        make_combinations(0, [])
        
        return result
```


<a name="4y12X"></a>
### 总结
回溯算法真的有套路的～～
```python
class Solution(object):
    def function(self, nums):
        if ...........
		other parma
        def backtrack(....):
            if ....: res.append(...)
            for i in range(...):
                backtrack(.....)
        backtrack(....)# 初始化
        return res
```
