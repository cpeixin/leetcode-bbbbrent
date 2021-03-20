
哈希表-映射-集合-二叉树-堆<br />![v2-820fa01be2dfcc080ec67d00ed9efd55_1440w.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/1072113/1592554431322-a01740ce-a5e4-4496-b2a0-a7130a6f607c.jpeg#align=left&display=inline&height=829&margin=%5Bobject%20Object%5D&name=v2-820fa01be2dfcc080ec67d00ed9efd55_1440w.jpg&originHeight=829&originWidth=1440&size=239867&status=done&style=none&width=1440)<br />堆：可以迅速找到最大值或者最小值的数据结构<br />

<a name="whc7H"></a>
### 解题思路
<a name="Mb05R"></a>
#### [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
这道题容易想到使用Map哈希表来实现，但是居然忘记了基本的排序实现方法，而且如果在面试中遇到，直接使用下面的方式，是不是有些太取巧了。借助Map哈希表来实现，在python中可以直接定义defaultdict，这样在遍历的过程中，会减少一些判断的步骤
```python
class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        word_count_dict = collections.defaultdict(int)
        for index in range(len(s)):
            dict[s[index]]+=1
            dict[t[index]]-=1
        for value in dict.values():
            if value != 0:
                return False
        return True
```
<a name="IKlKd"></a>
#### 
<a name="O7rLG"></a>
#### [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)
和上一题思路相同，但是这里需要同时用到排序和哈希表，这里需要注意一点，Python语言的话，defaultdict(list)和dict[tuple(key)]
```python
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dict = collections.defaultdict(list)
    for str in strs:
        dict[tuple(sorted(str))].append(str)
    return dict.values()
```
**复杂度分析**<br />**时间复杂度：O(NKlogK)**，其中 N 是 strs 的长度，而 K 是 strs 中字符串的最大长度。当我们遍历每个字符串时，外部循环具有的复杂度为 O(N)。然后，我们在 O(KlogK) 的时间内对每个字符串排序。<br />**空间复杂度：O(NK)**，排序存储在 ans 中的全部信息内容。<br />

<a name="pQ9I0"></a>
#### [数对和](https://leetcode-cn.com/problems/pairs-with-sum-lcci/)
核心思想可以利用“两数之和”的思想，核心计算也是相似的，但是这里要注意：<br />**输入:** nums = [5,6,5,6], target = 11<br />**输出: **[[5,6],[5,6]]<br />
<br />找出所有能组合的数对，并且像[5,5,5,6]这样的测试用例，5的次数要保留，所以Map的涉及。{key: num}，num要动态增减，来匹配尽可能多的组合。
```python
class Solution(object):
    def pairSums(self, nums, target):
        sum_dict = collections.defaultdict(int)
        res = []
        for index in range(len(nums)):
            if sum_dict.get(target-nums[index],0)==0:
                dict[num[index]] = dict.get(nums[index],0)+1
            else:
                res.append([target-nums[index], nums[index]])
                dict[target-nums[index]]-=1
        return res
        
```
**复杂度分析**<br />**时间复杂度：O(N)**<br />**空间复杂度：O(N)**<br />

<a name="SCzCV"></a>
#### [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)
二叉树遍历的前、中、后序递归写法，一定要背熟。
```python
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root,res)
        return res


    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
```
<a name="CEnj5"></a>
#### 复杂度分析
**时间复杂度**：O(n)。递归函数 T(n)=2⋅T(n/2)+1。<br />**空间复杂度**：最坏情况下需要空间O(n)，当二叉树为平衡二叉树时，它的高度为 log⁡(N)，平均情况为O(logn)。
<a name="nJ0EV"></a>
#### 
<a name="upKgR"></a>
#### [N叉树的前、后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
有别于二叉树，N叉树在结构方面则没有left，right节点的。而是统一为children节点
```python
def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
```

<br />调用递归函数时，递归函数内部则应遍历父节点下面的子节点
```python
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:return None
        self.helper(root, res)
        return res

    def helper(self, root, res):
        # res.append(root.val)前序遍历
        for node in root.children:
            self.helper(node, res)
        res.append(root.val)# 后序遍历
```
复杂度分析：<br />• **时间复杂度**：O(n)<br />• **空间复杂度**：O(n)<br />

<a name="lXjol"></a>
#### [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
```python
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right)+1
```
![WechatIMG107.jpeg](https://cdn.nlark.com/yuque/0/2020/jpeg/1072113/1592296223996-864bb6a7-8a61-4247-a9d9-91b91e827973.jpeg#align=left&display=inline&height=1080&margin=%5Bobject%20Object%5D&name=WechatIMG107.jpeg&originHeight=1080&originWidth=1440&size=157815&status=done&style=none&width=1440)<br />
<br />**复杂度分析**<br />**时间复杂度**：我们每个结点只访问一次，因此时间复杂度为 O(N)，其中 N是结点的数量。<br />**空间复杂度**：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。但在最好的情况下（树是完全平衡的），树的高度将是 log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))。<br />

<a name="pCp78"></a>
#### [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
注意题目！！注意审题！！<br />

> 给定一个二叉树，找出其最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数量。


<br />很多人写出的代码都不符合 1,2 这个测试用例，是因为没搞清楚题意，题目中说明:叶子节点是指没有子节点的节点，这句话的意思是 1 不是叶子节点，题目问的是到叶子节点的最短距离，所以所有返回结果为 1 当然不是这个结果，另外这道题的关键是搞清楚递归结束条件<br />
<br />叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点<br />当 root 节点左右孩子都为空时，返回 1<br />当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度<br />当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
```python
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
       	return min(self.minDepth(root.left), self.minDepth(root.right))+1
```

<br />**复杂度分析**<br />**时间复杂度**：我们访问每个节点一次，时间复杂度为 O(N) ，其中 N 是节点个数。<br />**空间复杂度**：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N （树的高度）次，因此栈的空间开销是 O(N) 。但在最好情况下，树是完全平衡的，高度只有 log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。<br />

<a name="B7Aa4"></a>
#### [左叶子之和](https://leetcode-cn.com/problems/sum-of-left-leaves/)
这个～～  只要递归条件一变，我准懵逼～～，多做几道看看能不能掌握一下规律～～。此题代码和上题代码结构好相似啊
```python
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
```
<a name="VY1uc"></a>
#### <br />
复杂度分析<br />时空复杂度均是O(n)
<a name="xeMsr"></a>
#### 
<a name="WBbVW"></a>
#### [最大二叉树](https://leetcode-cn.com/problems/maximum-binary-tree/)

<br />看了题目本身就是一个递归的问题，第一次的数组是[3,2,1,6,0,5] 取 6 作为根节点， 然后 [ 3, 2, 1] 作为 左子树， [0, 5] 作为右子树。然后重复上诉过程，把[3, 2,1] 和 [ 0, 5]当做是新的数组再进行一次重复<br />
<br />还是三部曲<br />
<br />1.递归终止条件 当左子树和右子树的数组都为空时<br />2.本次递归做什么 取出数组的最大值，并把数组根据最大值分成左右两个数组，然后进行递归赋值<br />3.返回子树的根节点<br />

```python
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if not nums: return None
    max_num = max(nums)
    max_index = nums.index(max_num)
    root = TreeNode(max_num)
    # 由于[3,2,1]为左子树，并且3为最大，所以为左子树root节点
    # 而此时constructMaximumBinaryTree(nums[0:0])，所以3下面没有左节点了。
    root.left = self.constructMaximumBinaryTree(nums[0:max_index])
    root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
    return root
```
复杂度分析<br />
<br />**时间复杂度：O(n^2)**，方法 constructMaximumBinaryTree 一共被调用 n 次。每次递归寻找根节点时，需要遍历当前索引范围内所有元素找出最大值。一般情况下，每次遍历的复杂度为 O(logn)，总复杂度为 O(nlogn)。最坏的情况下，数组 numsnums 有序，总的复杂度为 O(n^2)<br />
<br />**空间复杂度：O(n)**。递归调用深度为 nn。平均情况下，长度为 nn 的数组递归调用深度为 O(\log n)O(logn)。<br />

<a name="2VDsm"></a>
#### [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)
**<br />**从底至顶（提前阻断）**<br />此方法为本题的最优解法，但“从底至顶”的思路不易第一时间想到。<br />思路是对二叉树做先序遍历，从底至顶返回子树最大高度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。这里的核心条件是：**left-right < 2
```python
def isBalanced(self, root: TreeNode) -> bool:
    return recur(root)!=-1


def recur(self, root):
    if not root: return 0
    left = self.recur(root.left)
    if left == -1: return -1
    right = self.recur(root.right)
    if right == -1: return -1
    return max(left, right)+1 if abs(left-right)<2 else -1
```

<br />时间复杂度 O(N)： N 为树的节点数；最差情况下，需要递归遍历树的所有节点。<br />空间复杂度 O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。<br />
<br />**从顶至底（暴力法）**<br />**<br />此方法容易想到，但会产生大量重复计算，时间复杂度较高。<br />思路是构造一个获取当前节点最大深度的方法 depth(root) ，通过比较此子树的左右子树的最大高度差abs(depth(root.left) - depth(root.right))，来判断此子树是否是二叉平衡树。若树的所有子树都平衡时，此树才平衡。
```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```

<br />**复杂度分析：**<br />**时间复杂度 **O(Nlog_2 N)： 最差情况下， isBalanced(root) 遍历树所有节点，占用 O(N)；判断每个节点的最大高度 depth(root) 需要遍历 各子树的所有节点 ，子树的节点数的复杂度为 O(log_2 N)<br />**空间复杂度 **O(N)： 最差情况下（树退化为链表时），系统递归需要使用 O(N) 的栈空间。<br />

<a name="yuSus"></a>
#### [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
这道题知道用递归做，但是递归函数无从从从从下手～～<br />![image.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1592553146422-2d2b4c01-a50a-4842-a761-4aaf449d20c6.gif#align=left&display=inline&height=543&margin=%5Bobject%20Object%5D&name=image.gif&originHeight=543&originWidth=773&size=456834&status=done&style=none&width=773)<br />其实就是交换一下左右节点，然后再递归的交换左节点，右节点<br />根据动画图我们可以总结出递归的两个条件如下：<br />
<br />终止条件：当前节点为null时返回<br />交换当前节点的左右节点，再递归的交换当前节点的左节点，递归的交换当前节点的右节点
```python
def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 递归函数的终止条件，节点为空时返回
		if not root:
			return None
		# 将当前节点的左右子树交换
		root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
		self.invertTree(root.left)
		self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了		
		return root
```

<br />时间复杂度：每个元素都必须访问一次，所以是O(n)<br />空间复杂度：最坏的情况下，需要存放O(h)个函数调用(h是树的高度)，所以是O(h)<br />
<br />

<a name="h6cwI"></a>
#### [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

<br />**思路和算法**<br />其他语言的话，我们用一个大根堆实时维护数组的前 kk 小值。首先将前 kk 个数插入大根堆中，随后从第 k+1 个数开始遍历，如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。最后将大根堆里的数存入数组返回即可。<br />
<br />而 Python 语言中的为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 kk 小值。<br />
<br />例如测试用例：arr = [3,2,1], k = 2<br />
<br />不取相反数的小顶堆：<br />2<br />3<br />这是1则是和堆顶2比较，2出堆，则不满足题目要求，返回【1，3】，不是最小的。如果去相反数，则是：<br />-3<br />-2<br />这时则是类似大顶堆，实际较大的数（相反数较小）的在堆顶，这是 1与-（-3）进行比较，如果小于堆顶，则堆顶出堆，实则大树出堆。<br />
<br />**复杂度分析**<br />时间复杂度：O(nlogk)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，最坏情况下数组里 n 个数都会插入，所以一共需要 O(nlogk) 的时间复杂度。<br />空间复杂度：O(k)，因为大根堆里最多 k个数。
```python
def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    if k==0: return list()
    hp = [-elem for elem in arr[:k]]
    heapq.heapify(hp)
    for index in range(k, len(arr)):
        if arr[index] < -hp[0]:
            heapq.heappop(hp)
            heapq.heappush(hp, -arr[index])
            
    result = [-elem for elem in hp]
    return result
```


<a name="jR2wt"></a>
#### [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)
这道题上周我们是通过双端队列来做的，学了“堆”之后，也是可以使用堆来做的，python中实现的堆，是小顶堆，所以对于求最小最大，要灵活运用 相反数 来求解。<br />
<br />这道题用双端队列来实现，时间复杂度是O(n)，空间复杂度是O(k)，利用堆来实现，时间复杂度是O(nlogn)，空间复杂度是O（n）,所以还是双端队列的实现方式要优于堆实现。
```python
res, heap = [], []
		for i in range(len(nums)):
			heapq.heappush(heap, ( -nums[i], i))
			if i + 1 >= k:
				while heap and heap[0][1] <  i + 1 - k:
					heapq.heappop(heap)
				res.append(-heap[0][0])
		return res
```


<a name="t6kZR"></a>
#### [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)
给定一个非空的整数数组，返回其中出现频率前 **_k _**高的元素。首先，需要借助Map来统计频数，再将（dict[key], key）写入堆，heapq.heappush()。最后pop()出k个元素放到结果中。
```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []: return []
        dict = collections.defaultdict(int)
        for num in nums:
            dict[num]+=1
        res, hp = [], []
        for key in dict.keys():
            heapq.heappush(hp, (-dict[key], key))

        count = 0
        while count<k:
            num, key = heapq.heappop(hp)
            res.append(key)
            count+=1
        return res
```
Time: O(NlogN)<br />Space: O(N)<br />

<a name="V7sE4"></a>
#### [有序矩阵中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/)
此题中涉及到一个n*n矩阵，那么就会涉及到一个双层遍历。看了很对解法，基本上如果用堆来实现，都避免不了双层的遍历添加到堆。<br />
<br />维护一个k大小的堆，那么取第K小的，则就是heap[0]
```python
def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    if not matrix:
        return None
    heap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            next_value = -matrix[row][col]
            if len(heap) < k：
            	heapq.heappush(heap, next_value)
            elif next_value > heap[0]:
                heapq.heappushpop(heap, next_value)
    return -heap[0]
            
```
时间复杂度为O(n^2log(k))，空间复杂度为O(k)。

<a name="NRPjm"></a>
#### [丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/)

<br />很容易想到的方法是：从1起检验每个数是否为丑数，直到找到n个丑数为止。但是随着n的增大，绝大部分数字都不是丑数，我们枚举的效率非常低。因此，换个角度思考，如果我们只生成丑数，且生成n个，这道题就迎刃而解。<br />
<br />不难发现生成丑数的规律：如果已知丑数ugly，那么ugly * 2，ugly * 3和ugly * 5也都是丑数。<br />既然求第n小的丑数，可以采用最小堆来解决。每次弹出堆中最小的丑数，然后检查它分别乘以2、3和 5后的数是否生成过，如果是第一次生成，那么就放入堆中。第n个弹出的数即为第n小的丑数。<br />
<br />**算法流程**<br />创建最小堆heap，哈希表 seen（set（））和质因数列表factors = [2, 3, 5]。heap用于存储已生成的丑数，弹出最小值；seen用于标记堆中出现过的元素，避免重复入堆。<br />初始化将1入堆，并添加到seen。<br />重复以下步骤n次：<br />弹出堆中最小的数字 curr_ugly。<br />对于factors中每个因数f，生成新的丑数new_ugly。若new_ugly不在seen中，则将其添加到heap中并更新seen。<br />curr_ugly即为第n小的丑数，返回。<br />

```python
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        heap, ugly_num_set = [], set()
        # 初始化
        heapq.heappush(heap, 1)
        ugly_num_set.add(1)
        # 丑数因子
        factors = [2,3,5]
        current_ugly = 1
        
        for index in range(n):
            current_ugly = heapq.heappop(heap)
            for factor in factors:
                new_ugly = factor*current_ugly
                # 防止丑数重复
                if new_ugly not in ugly_num_set:
                    ugly_num_set.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return current_ugly
```

<br />**复杂度分析**<br />**时间复杂度**：O(nlogn)。弹出每个最小值时，时间复杂度都为堆的高度，因此时间复杂度为O(nlogn)。<br />**空间复杂度**：O(n)。遍历n个丑数，并将每个丑数乘以2、3和5的结果存入堆中。堆和哈希表的元素个数都不会超过n * 3。
<a name="oYdNU"></a>
### 总结

- 两数之和相关的题，考虑用哈希表
- 最小K，最大K值，考虑用堆。
- 关于递归，虽然多度几遍，就能看懂，但是执行的步骤则看着看着就乱了。下面有个带着分析过程的视频，个人感觉很好，能帮助理解。[https://www.bilibili.com/video/BV1g741137Wq?from=search&seid=8033860015351616278](https://www.bilibili.com/video/BV1g741137Wq?from=search&seid=8033860015351616278)
