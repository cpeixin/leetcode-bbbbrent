<a name="jqo2o"></a>
## 大纲
深度优先：借用栈<br />广度优先：借用队列<br />
<br />贪心算法的难点在于，怎么证明某个题目可以使用贪心法。

- 有时可以正常的去使用贪心算法
- 有时则需要稍微进行转化，使用贪心
- 有时需要从前向后贪心
- 有时需要从后向前贪心


<br /> 二分法模板<br />
![截屏2020-07-05 上午11.05.55.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593951039266-be0808e3-bd16-40b9-8f95-9130f7158b3d.png#align=left&display=inline&height=1018&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-05%20%E4%B8%8A%E5%8D%8811.05.55.png&originHeight=1018&originWidth=1868&size=743863&status=done&style=none&width=1868)
```python

left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```


<a name="bVyrB"></a>
## 解题思路
<a name="HO9Uk"></a>
### 深度优先广度优先系列


<a name="bwDYJ"></a>
#### [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
BFS
```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], [root]
        while queue:
            tmp = []
            for index in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
```
复杂度分析<br />记树上所有节点的个数为 nn。<br />时间复杂度：每个点进队出队各一次，故渐进时间复杂度为 O(n)。<br />空间复杂度：队列中元素的个数不超过 n 个，故渐进空间复杂度为 O(n)<br />

<a name="sOn4N"></a>
#### [在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)
DFS，和回溯法几乎一样啊
```python
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def DFS(root, level):
            if not root: return []
            if len(res) <= level:
                res.append(float('-inf'))
            res[level] = max(res[level], root.val)
            DFS(root.left, level+1)
            DFS(root.right, level+1)
        DFS(root, 0)
        return res
        
```
BFS
```python
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res, queue = [], [root]
        while queue:
            max_num = float('-inf')
            for index in range(len(queue)):
                node = queue.pop(0)
                max_num = max(max_num, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(max_num)
        return res
```
复杂度分析：<br />时间复杂度： O(N)，遍历树中所有节点。<br />空间复杂度： DFS 是 O(Height)，为树的高度，最好完全二叉树 O(log(N))，最坏链表 O(N)；BFS 就是某层最大节点个数。<br />

<a name="hvaxh"></a>
#### [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
DFS
```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def DFS(left, right, tmp):
            if left == 0 and right == 0: res.append(tmp)
            if left > 0:DFS(left-1, right, tmp+'(')
            if right > left: DFS(left, right-1, tmp+')')
        DFS(n, n, '')
        return res
```
![截屏2020-06-29 下午9.19.21.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593439878745-947f1f3f-f76f-4462-95b4-ec2f2131f347.png#align=left&display=inline&height=452&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-29%20%E4%B8%8B%E5%8D%889.19.21.png&originHeight=452&originWidth=1586&size=129284&status=done&style=none&width=1586)<br />
<br />

<a name="KRKAt"></a>
#### [单词接龙](https://leetcode-cn.com/problems/word-ladder/)
[题解](https://leetcode-cn.com/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/)<br />![截屏2020-06-29 下午10.55.27.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593442565409-177decbb-b59c-4b04-af56-558806c5cb9a.png#align=left&display=inline&height=1310&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-06-29%20%E4%B8%8B%E5%8D%8810.55.27.png&originHeight=1310&originWidth=1636&size=329556&status=done&style=none&width=1636)<br />BFS
```python
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)
```
<a name="brALH"></a>
#### 
<a name="Hne38"></a>
#### [二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)
本问题是典型的二叉树方案搜索问题，使用回溯法解决，其包含 先序遍历 + 路径记录 两部分。<br />
<br />先序遍历： 按照 “根、左、右” 的顺序，遍历树的所有节点。<br />路径记录： 在先序遍历中，记录从根节点到当前节点的路径。当路径为 ① 根节点到叶节点形成的路径 且 ② 各节点值的和等于目标值 sum 时，将此路径加入结果列表。<br />
<br />算法流程：<br />pathSum(root, sum) 函数：<br />
<br />初始化： 结果列表 res ，路径列表 path 。<br />返回值： 返回 res 即可。<br />recur(root, tar) 函数：<br />
<br />递推参数： 当前节点 root ，当前目标值 tar 。<br />终止条件： 若节点 root 为空，则直接返回。<br />递推工作：

- 路径更新： 将当前节点值 root.val 加入路径 path ；
- 目标值更新： tar = tar - root.val（即目标值 tar 从 sum 减至 00 ）；
- 路径记录： 当 ① root 为叶节点 且 ② 路径和等于目标值 ，则将此路径 path 加入 res 。
- 先序遍历： 递归左 / 右子节点。
- 路径恢复： 向上回溯前，需要将当前节点从路径 path 中删除，即执行 path.pop()
```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [],[]
        def recur(root, sum):
            if not root: return None
            path.append(root.val)
            sum-=root.val
            if sum==0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, sum)
            recur(root.right, sum)
            path.pop()
        recur(root, sum)
        return res
```
复杂度分析：<br />时间复杂度 O(N) ： N 为二叉树的节点数，先序遍历需要遍历所有节点。<br />空间复杂度 O(N)： 最差情况下，即树退化为链表时，path 存储所有树节点，使用 O(N) 额外空间。<br />

<a name="kCuWV"></a>
#### [从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)
BFS<br />从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
```python
例如:
给定二叉树: [3,9,20,null,null,15,7],
   3
  / \
 9  20
   /  \
  15   7
返回：
[3,9,20,15,7]
```


```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        queue = [root]
        while queue:
            for index in range(len(queue)):
                node = queue.pop(0)
                res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res
```
复杂度分析：<br />时间复杂度 O(N) ： N 为二叉树的节点数量，即 BFS 需循环 N 次。<br />空间复杂度 O(N) ： 最差情况下，即当树为平衡二叉树时，最多有 N/2 个树节点同时在 queue 中，使用 O(N) 大小的额外空间。<br />

<a name="yGToM"></a>
#### [从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)
BFS
```python
例如:
给定二叉树: [3,9,20,null,null,15,7],
   3
  / \
 9  20
   /  \
  15   7
返回：
[
  [3],
  [9,20],
  [15,7]
]
```


```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], [root]
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
```
复杂度分析：<br />时间复杂度 O(N)： N为二叉树的节点数量，即 BFS 需循环 NN 次。<br />空间复杂度 O(N)： 最差情况下，即当树为平衡二叉树时，最多有 N/2个树节点同时在 queue 中，使用 O(N) 大小的额外空间。<br />
<br />

<a name="1Yqj6"></a>
#### [从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)
BFS
```python
例如:
给定二叉树: [3,9,20,null,null,15,7],
   3
  / \
 9  20
   /  \
  15   7
返回：
[
  [3],
  [20,9],
  [15,7]
]
```
```python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, queue = [], collections.deque([root])
        while queue:
            tmp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(list(tmp))
        return res
```
复杂度分析：<br />时间复杂度 O(N) ： N 为二叉树的节点数量，即 BFS 需循环 N 次，占用 O(N) ；双端队列的队首和队尾的添加和删除操作的时间复杂度均为 O(1)。<br />空间复杂度 O(N) ： 最差情况下，即当树为满二叉树时，最多有N/2 个树节点 同时 在 deque 中，使用 O(N) 大小的额外空间。<br />

<a name="016h0"></a>
#### [火柴拼正方形](https://leetcode-cn.com/problems/matchsticks-to-square/)
不看题解，一辈子都想不出来的解法，回撤的那一步注意注意！！！！
```python
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        # 可以理解成目前数组可以构成的正方形周长
        square_length = sum(nums)
        # 数组的长度
        nums_size = len(nums)
        # 可能的正方形边长, //整除得到的最大整数
        possible_side = square_length // 4
        # 判断是否与上面计算的周长相等
        if possible_side*4 != square_length: return False
        # 构建存储四条边结构
        sides = [0 for _ in range(4)]
        # 对数组进行排序，降序排列有利于计算，类似于剪枝
        nums.sort(reverse=True)
        # 定义递归回溯函数
        def backtrack(index):
            # 长度全部遍历完，如果四条边相等，则可以构成正方形
            if index == nums_size:
                return sides[0] == sides[1] == sides[2] == possible_side
            for i in range(4):
                # 如果当前i边满足了possible_side可能边大小长度，则遍历下一个边
                if sides[i]+nums[index] <= possible_side:
                    sides[i]+=nums[index]
                    if backtrack(index+1): return True
                    # 不可缺少的一步，回撤
                    sides[i]-=nums[index]
            return False
        #实例化的同时，判断返回结果
        return backtrack(0)
```
复杂度分析<br />时间复杂度：O(4^N)，其中 N 是火柴的数量。在进行搜索之前，我们可以将火柴的长度从大到小进行排序，方便我们先搜索较长的火柴。这样做的目的是对搜索进行剪枝，例如当火柴的长度为 [4,4,4,8] 时，每条边的长度为 5，如果我们先搜索长度为 8 的火柴，就可以发现它无法被放在任意一组中，因此直接退出搜索返回 False。<br />**空间复杂度：O(N)**。<br />

<a name="hKjvJ"></a>
#### [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)
题解：<br />给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。<br />此题可用DFS，BFS，并查集<br />
<br />[https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/](https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/)<br />
<br />代码：<br />**DFS**
```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j, rows, columns):
            # 越界判断
        	if not 0<=i<rows or not 0<=j<columns or grid[i][j] == '0': return
            # 赋0这一步很妙！！！
            grid[i][j]=0
            dfs(grid, i+1, j, rows, columns)
            dfs(grid, i-1, j, rows, columns)
            dfs(grid, i, j+1, rows, columns)
            dfs(grid, i, j-1, rows, columns)
        
        # 岛屿计数
        count = 0
        # 行
        rows = len(grid)
        if rows == 0: return 0
        # 列
        columns = len(grid[0])
        # 遍历每一个元素
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    count+=1
                    dfs(grid, i, j, rows, columns)
        return count
        
```
**BFS**
```python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count
```

<br />复杂度分析：<br />
<br />**总结反思：**<br />还是没有掌握DFS的根髓<br />
<br />
<br />

<a name="fNBaw"></a>
### 贪心算法系列
<a name="I1Lmw"></a>
#### 
<a name="koraL"></a>
#### [分发饼干](https://leetcode-cn.com/problems/assign-cookies/)
**题解**<br />爱的太多容易伤到自己，爱的太少容易伤到别人，爱要贪心，更要刚刚好 hahaha<br />此题两个思想： 

- 先满足需求度小的孩子
- 先用小的饼干去满足孩子

所以对饼干和孩子需求度进行升序排列<br />
<br />更多方法的题解：[https://leetcode-cn.com/problems/assign-cookies/solution/tan-xin-suan-fa-you-xian-dui-lie-python-dai-ma-by-/](https://leetcode-cn.com/problems/assign-cookies/solution/tan-xin-suan-fa-you-xian-dui-lie-python-dai-ma-by-/)<br />
<br />**代码**
```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 边界判断
        if not g or not s: return 0
        # 排序，上面的两个思想
        g.sort()
        s.sort()
        #  初始化孩子和饼干的数量
        child, cookies = 0, 0
        while child < len(g) and cookies < len(s):
            # 如果当前孩子的饼干需求小于我们此次选择的，则满足条件
            if g[child] <= s[cookies]:
                child+=1
            # 无论是否满足，饼干数都要后移
            # 1.满足：则后移下一个饼干
            # 2.不满足：当前小的饼干不满足，则后移取更大一点的饼干与当前孩子的需求相比
            cookies+=1
        return child
```

<br />**复杂度分析**<br />时间复杂度：O(nlogn)  (待商榷)<br />空间复杂度：O(n)<br />
<br />**总结**<br />
<br />
<br />股票系列一共 6 道题，其实下面是利用动态规划来实现的：<br />
<br />LeetCode 121 [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)：最多进行 1 笔交易（k=1）<br />LeetCode 122[买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)：不限交易次数（k=+inf）【二维 DP】

- LeetCode 309[最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)：不限交易次数（k=+inf），但有「冷冻期」的额外条件
- LeetCode 714[买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)：不限交易次数（k=+inf），但有「手续费」的额外条件

LeetCode 123[买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)：最多进行 2 笔交易（k=2）【三维 DP】<br />LeetCode 188[买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)：最多进行 k 次交易<br />

<a name="KeQXf"></a>
#### [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)
题解<br />根据labaladong的股票类算法模板，这里更为详细。<br />[团灭股票类问题](https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.md)<br />关于状态方程的转换，liweiwei解释的也很好<br />![截屏2020-07-04 下午4.45.25.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1593852395820-4276e6db-1641-40f5-9835-71bd01a37385.png#align=left&display=inline&height=1122&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-04%20%E4%B8%8B%E5%8D%884.45.25.png&originHeight=1122&originWidth=1666&size=252391&status=done&style=none&width=1666)<br />代码
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1: return 0
        dp = [[None, None] for _ in range(n)]
        # base case:
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]
```
**复杂度分析**<br />时间复杂度：O(n)<br />空间复杂度：O(n),空间优化以后相当于只用了 2 个变量
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 价格数组长度
        n = len(prices)

        """
        base case初始值:
        dp[-1][k][0] = dp[i][0][0] = 0
        dp[-1][k][1] = dp[i][0][1] = float('-inf')
        是经过分析题的过程中，总结出来的
        下面两个变量的命名，profit_i_(0 or 1), i代表的是天数，0，1后缀代表的是，当前时候持有股票，0：没有持有，1：持有
        定义下面两个变量则可以表示当前的两种状态， 要么持有股票，要么没有持有股票
        """
        profit_i_0 = 0
        profit_i_1 = float('-inf')
        # 遍历每一天
        for i in range(n):
            """
            状态转移方程：
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            下面两行核心计算步骤就是上面的状态方程转换过来的。这里注意 k-1 ，我们这里将 买入操作 进行减1，也就是减少一次交易次数，dp[i-1][k-1][0]为0，则省去
            """
            profit_i_0 = max(profit_i_0, profit_i_1+prices[i])# max(选择rest,选择sell)
            profit_i_1 = max(profit_i_1, -prices[i])# max(选择rest,选择buy)
        return profit_i_0
```
**<br />**复杂度分析**<br />时间复杂度：O(n)<br />空间复杂度：O(1),空间优化以后相当于只用了 2 个变量<br />
<br />**总结**<br />这题的核心是上面的状态方程，根据详细的解释，才能理解状态方程的意思，直接看，肯定看不懂<br />

<a name="C1uUA"></a>
#### [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)
**题解**<br />**<br />每天都有三种动作：买入（buy）、卖出（sell）、无操作（rest）。<br />
<br />因为不限制交易次数，因此交易次数这个因素不影响题目，不必考虑。DP Table 是二维的，两个维度分别是天数（0,1,...,n-1）和是否持有股票（1 表持有，0 表不持有）。<br />
<br />状态转移方程<br />**Case 1，今天我没有股票，有两种可能：**

- 昨天我手上就没有股票，今天不做任何操作（rest）；
- 昨天我手上有一只股票，今天按照时价卖掉了（sell），收获了一笔钱

**Case 2，今天持有一只股票，有两种可能：**

- 昨天我手上就有这只股票，今天不做任何操作（rest）；
- 昨天我没有股票，今天按照时价买入一只（sell），花掉了一笔钱


<br />综上，第 i 天的状态转移方程为：
```python
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
```

<br />注意上面的转移方程只是对某一天而言的，要求出整个 DP Table 的状态，需要对 i 进行遍历。<br />
<br />**边界状态**<br />观察状态转移方程，第 i 天的状态只由第 i-1 天状态推导而来，因此边界状态只需要定义 i=0（也就是第一天）即可：
```python
dp[0][0] = 0        # 第一天没有股票，说明没买没卖，获利为0
dp[0][1] = -prices[0]   # 第一天持有股票，说明买入了，花掉一笔钱
```

<br />**代码**
```python
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n<=1: return 0
        # dp table
        dp = [[None, None] for _ in range(n)]

        """
        边界条件，初始条件
        第 i 天的状态只由第 i-1 天状态推导而来，因此边界状态只需要定义 i=0（也就是第一天）
        """
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        #
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]# 返回最后一天且手上没有股票时的获利情况
```

<br />**复杂度分析**<br />时间复杂度：O(N)，这里 N 表示股价数组的长度。<br />空间复杂度：O(1)，分别使用两个滚动变量，将一维数组状态压缩到常数。<br />
<br />**总结**<br />
<br />

<a name="MTN8V"></a>
#### [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
题解：<br />这道题的在 [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) 的基础上添加了冷冻期的要求，即每次 sell 之后要等一天才能继续交易。状态转移方程要做修改，如果第 i 天选择买入股票，状态要从第 i-2 的转移，而不是 i-1 (因为第 i-1 天是冷冻期)。另外，由于状态转移方程中出现了 dp[i-2] 推导 dp[i-1]，因此状态边界除了考虑 i=0 天，**还要加上 i=1 天的状态。**Solution 如下<br />
<br />代码：
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0

        dp = [[None, None] for _ in range(n)]

        """
        如果第 i 天选择买入股票，状态要从第 i-2 的转移，而不是 i-1 (因为第 i-1 天是冷冻期)。
        另外，由于状态转移方程中出现了 dp[i-2] 推导 dp[i-1]，因此状态边界除了考虑 i=0 天，还要加上 i=1 天的状态。
        """
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], dp[0][0] - prices[1])
        
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        return dp[-1][0]
```
复杂度分析：<br />
<br />总结：<br />

<a name="BTAuu"></a>
#### [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
题解：<br />这道题在 [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)的基础上添加了交易费的要求，可以理解为每次 sell 时要缴纳一定的费用。边界状态保持不变，状态转移方程需要做修改。Solution 如下<br />
<br />代码：
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n<=1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)  # 卖出股票时注意要缴手续费
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]
```
当然，也可以买入的时候缴纳手续费：
```python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]-fee

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i][0]-prices[i]-fee)
        return dp[-1][0]
```

<br />复杂度分析：<br />时间复杂度：O(N)，这里 N 是股价数组的长度；<br />空间复杂度：O(N)，状态数组有 N 行，2 列。2 为常数，在计算复杂度的时候视为 1。<br />
<br />总结：<br />这里空间复杂度是可以优化到O(1)的，但是感觉没有二维dp看起来清楚，面试的时候可以可面试官沟通。<br />[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/dong-tai-gui-hua-by-liweiwei1419-6/](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/dong-tai-gui-hua-by-liweiwei1419-6/)<br />

<a name="YPZma"></a>
#### [买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)
**题解**<br />题目约定最多交易次数 k=2，因此交易次数必须作为一个新的维度考虑进 DP Table 里，也就是说，这道题需要三维 DP 来解决。三个维度分别为：天数 i（i=0,1,...,n-1），买入股票的次数 j（j=1,2,...,k）和是否持有股票（1 表持有，0 表不持有）. 特别注意买入股票的次数为 j 时，其实隐含了另一个信息，就是卖出股票的次数为 j-1 或 j 次。<br />
<br />状态转移方程，这里还是比较难懂，读了几遍，我的理解是，下面第一行代码，右边表示的是，昨天持有股票，但是今天没有持有，所以卖掉，卖掉没有影响k的次数。但是第二行代码的右边，昨天没有持有股票而今天有持有，则是今天🈶购买股票，昨天没有购买的情况下，则对应的k为k-1
```python
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i]) 
# 右边:今天卖了昨天持有的股票，所以两天买入股票的次数都是j
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i]) 
# 右边:昨天没有持股而今天买入一只，故昨天买入的次数是j-1
```
注意上面的转移方程只是穷举了第三个维度，要求出整个 DP Table 的状态，需要对 i 和 j 进行遍历。<br />
<br />边界状态<br />观察状态转移方程知，边界状态需要考虑两个方面：i=0 和 j=0
```python
# j=0 
for i in range(n):
    dp[i][0][0] = 0  # 没有买入过股票，且手头没有持股，则获取的利润为0
    dp[i][0][1] = -float('inf')	# 没有买入过股票，不可能持股，用利润负无穷表示这种不可能
# i=0
for j in range(1, k+1):	# 前面j=0已经赋值了，这里j从1开始
    dp[0][k][0] = 0	
    dp[0][k][1] = -prices[0]
```

<br />特别注意，上述两轮边界定义有交集——dp[0][0][0] 和 dp[0][0][1] ，后者会得到不同的结果，应以 j=0 时赋值结果为准。
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        # 题目指定为交易两次  所以没有采取遍历，而是将两次交易的状态方程写出来
        profit_i_1_0, profit_i_1_1 = 0, float('-inf')
        profit_i_2_0, profit_i_2_1 = 0, float('-inf')
        
        for i in range(n):
            profit_i_1_0 = max(profit_i_1_0, profit_i_1_1+prices[i])
            profit_i_1_1 = max(profit_i_1_1, -prices[i])
            profit_i_2_0 = max(profit_i_2_0, profit_i_2_1+prices[i])
            profit_i_2_1 = max(profit_i_2_1, profit_i_1_0-prices[i])
        return profit_i_2_0
```
遍历写法：
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0
        # dp table
        dp = [[[None, None] for _ in range(3)] for _ in range(n)]

        """边界条件，分别为i=0, k=0"""
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for k in range(3):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        # 这里注意：i=0， k=0在上面已经计算过了。所以这里的下标从1开始
        for i in range(1,n):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[-1][-1][0]

```

<br />**复杂度分析**<br />
<br />**总结：**<br />

<a name="mjQ73"></a>
#### [买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)
题解：给定一个数组，它的第_ i_ 个元素是一支给定的股票在第 _i _天的价格。<br />设计一个算法来计算你所能获取的最大利润。你最多可以完成 **k** 笔交易。<br />
<br />这道题理论上和 LeetCode 123（交易次数最多为2） 的解法一样，但是直接提交容易出现超内存的错误，是 DP Table 太大导致的。<br />
<br />有效的交易由买入和卖出构成，至少需要两天；反之，当天买入当天卖出则视为一次无效交易。如果题目给定的最大交易次数 k<=n/2，这个 k 是可以有效约束交易次数的；如果给定的 k>n/2 ，那这个 k 实际上起不到约束作用了，可以认为 k=+inf，本题退化为 LeetCode 122（不限交易次数） 。<br />
<br />题目整体思路是判断 k 和 n/2 的大小关系，两个分支分别用 LeetCode 123 和 LeetCode 122 的代码解决，可有效防止内存超出。<br />
<br />代码：
```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1: return 0
        """
        正常交易的情况下，完成一次交易最少也需要两天的时间。所以有效的交易次数应该小于等于 n//2
        如果大于 n//2 ，则此种情况退化为可交易任意次的情况
        """
        if k > n // 2:
            dp_1 = [[None, None] for _ in range(n)]
            #           # 边界条件
            dp_1[0][0] = 0
            dp_1[0][1] = -prices[0]

            for i in range(1, n):
                dp_1[i][0] = max(dp_1[i - 1][0], dp_1[i - 1][1] + prices[i])
                dp_1[i][1] = max(dp_1[i - 1][1], dp_1[i - 1][0] - prices[i])
            return dp_1[-1][0]
        else:
            dp_2 = [[[None, None] for _ in range(k+1)] for _ in range(n)]
            """边界条件，分别为i=0, k=0"""
            for i in range(n):
                dp_2[i][0][0] = 0
                dp_2[i][0][1] = float('-inf')
            for k in range(k+1):
                dp_2[0][k][0] = 0
                dp_2[0][k][1] = -prices[0]
            
            for i in range(1, n):
                for k in range(1, k+1):
                    dp_2[i][k][0] = max(dp_2[i-1][k][0], dp_2[i-1][k][1] + prices[i])
                    dp_2[i][k][1] = max(dp_2[i-1][k][1], dp_2[i-1][k-1][0] - prices[i])
            
            return dp_2[-1][-1][0]
```
复杂度分析：<br />
<br />
<br />总结：<br />首先这题限定了交易K次。和[买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)好像一样哈，只不过另一题限定了k=2，看其他高分解答，如果直接使用[买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)代码，会超出内存

所以对k值的判断很关键，k>n//2时，则k大于prices中正常的交易次数，此时，可以理解为k为任意数，则使用[买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

k<=2时，就满足了[买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)这道题的套路。最后就是将这两道题的套路合并在一起。

最后，不要忘记判断  if n <= 1 : return 0

<a name="OzqZU"></a>
### 二分查找
<a name="hLbDN"></a>
#### [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)
题解：首先我们要确定，这道题可不可以用二分查找。x = i^2，x为抛物线，i为单调递增，并且存在上下界。<br />
<br />代码：
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x
        while left <= right:
            mid = left+(right-left)//2
            if mid*mid == x: return mid
            elif mid*mid > x: right = mid - 1
            else: left = mid + 1
        # 退出条件为left>right
        return right
```
复杂度分析：<br />
<br />时间复杂度：O(logN)，二分法的时间复杂度是对数级别的。<br />空间复杂度：O(1)，使用了常数个数的辅助空间用于存储和比较。<br />
<br />总结：<br />代码中 `left + (right - left) // 2` 就和 `(left + right) / 2` 的结果相同，但是有效防止了 `left` 和 `right` 太大直接相加导致溢出。<br />
<br />关于边界问题，还需要进一步总结规律，例如这道题，left定义为0或者1都是可以的。

---

<a name="2LJmN"></a>
### 总结

<br />[团灭二分查找](https://github.com/cpeixin/leetcode-bbbbrent/blob/master/binary_search/%E5%9B%A2%E7%81%AD%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md)<br />
<br />DFS代码模版<br />[https://shimo.im/docs/UdY2UUKtliYXmk8t/read](https://shimo.im/docs/UdY2UUKtliYXmk8t/read)<br />BFS代码模板<br />[https://shimo.im/docs/ZBghMEZWix0Lc2jQ/read](https://shimo.im/docs/ZBghMEZWix0Lc2jQ/read)
