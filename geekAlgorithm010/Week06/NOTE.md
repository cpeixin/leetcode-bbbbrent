什么样的问题适合用动态规划来解决呢？换句话说，动态规划能解决的问题有什么规律可循呢？实际上，动态规划作为一个非常成熟的算法思想，很多人对此已经做了非常全面的总结。我把这部分理论总结为“**一个模型三个特征**”。<br />
<br />首先，我们来看，什么是“一个模型”？它指的是动态规划适合解决的问题的模型。我把这个模型定义为“**多阶段决策最优解模型**”。<br />
<br />下面我具体来给你讲讲。我们一般是用动态规划来解决最优问题。而解决问题的过程，需要经历多个决策阶段。每个决策阶段都对应着一组状态。然后我们寻找一组决策序列，经过这组决策序列，能够产生最终期望求解的最优值。<br />
<br />现在，我们再来看，什么是“三个特征”？它们分别是**最优子结构、无后效性和重复子问题**。<br />
<br />这三个概念比较抽象，我来逐一详细解释一下。<br />
<br />1. 最优子结构最优子结构指的是，问题的最优解包含子问题的最优解。反过来说就是，我们可以通过子问题的最优解，推导出问题的最优解。如果我们把最优子结构，对应到我们前面定义的动态规划问题模型上，那我们也可以理解为，后面阶段的状态可以通过前面阶段的状态推导出来。<br />
<br />2. 无后效性无后效性有两层含义，第一层含义是，在推导后面阶段的状态的时候，我们只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。第二层含义是，某阶段状态一旦确定，就不受之后阶段的决策影响。无后效性是一个非常“宽松”的要求。只要满足前面提到的动态规划问题模型，其实基本上都会满足无后效性。<br />
<br />3. 重复子问题这个概念比较好理解。前面一节，我已经多次提过。如果用一句话概括一下，那就是，不同的决策序列，到达某个相同的阶段时，可能会产生重复的状态。<br />
<br />动态规划的题目分为两大类，**一种是求最优解类，典型问题是背包问题，另一种就是计数类**<br />
<br />![截屏2020-07-15 下午6.05.03.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594807627765-af979c2d-fbce-417f-9152-cb9dce0c773a.png#align=left&display=inline&height=480&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-15%20%E4%B8%8B%E5%8D%886.05.03.png&originHeight=480&originWidth=1320&size=274903&status=done&style=none&width=1320)<br />

<a name="7D13x"></a>
### 解题思路
<a name="S0ip7"></a>
#### [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
题解：斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：F(0) = 0,   F(1) = 1 ,F(N) = F(N - 1) + F(N - 2), 其中 N > 1.<br />
<br />**代码：**<br />**最优写法：**
```python
class Solution(object):
    def fib(self, N):
        if N <= 1: return N
        dp0, dp1 = 0, 1
        for _ in range(2, N+1):
            dp2 = dp0 + dp1
            dp0 = dp1
            dp1 = dp2
        return dp2
```
**复杂度分析：本算法的时间复杂度是 O(n)。空间复杂度是 O(1)**<br />**<br />**上面这种写法是根据下面的这个写法来转换得到的**
```python
class Solution(object):
    def fib(self, N):
        if N<=1: return N
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```
**上面的两种解法是自底而上的dp数组循环，下面给出的是自顶向下递归法**
```python
class Solution(object):
    def fib(self, N):
        if N <= 1: return N
        dp = {0:0, 1:1}
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[N]
```
**但是这种方法利用dp数组空间复杂度为O(n)，所以才可以通过观察，每一个状态只和前两个状态有关，所以可以使用变量进行替换，提升空间复杂度。**<br />**<br />**<br />**总结：**<br />这个例子的细节优化。细心的读者会发现，根据斐波那契数列的状态转移方程，当前状态只和之前的两个状态有关，其实并不需要那么长的一个 DP table 来存储所有的状态，只要想办法存储之前的两个状态就行了。所以，可以进一步优化，把空间复杂度降为 O(1)。<br />有人会问，动态规划的另一个重要特性「最优子结构」，怎么没有涉及？下面会涉及。斐波那契数列的例子严格来说不算动态规划，因为没有涉及求最值，以上旨在演示算法设计螺旋上升的过程。<br />
<br />

<a name="FQtB6"></a>
#### [零钱兑换](https://leetcode-cn.com/problems/coin-change/)
**题解**：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。<br />**代码**：<br />**记忆化搜索，自顶向下**
```python
class Solution:
    def coinChange(self, coins, amount):
        #  初始化备忘录
        cache = {}
        def dp(tmp_amount):
            # 判断备忘录中是否存在
            if tmp_amount in cache: return cache[tmp_amount]
            # base case
            if tmp_amount == 0: return 0
            if tmp_amount < 0: return -1
            # 结果，初始化一个大数
            res = float('inf')
            for coin in coins:
                # 子问题，状态方程
                sub_problem = dp(tmp_amount - coin)
                if sub_problem == -1: continue
                res = min(res, sub_problem+1)
            # 存入备忘录
            cache[tmp_amount] = res if res != float('inf') else -1
            return cache[tmp_amount]
        return dp(amount)
```
**复杂度分析：**<br />**时间复杂度：O(Sn)**，其中 S 是金额，n 是面额数。我们一共需要计算 S 个状态的答案，且每个状态 F(S) 由于上面的记忆化的措施只计算了一次，而计算一个状态的答案需要枚举 n 个面额值，所以一共需要 O(Sn) 的时间复杂度。<br />**空间复杂度：O(S)**，我们需要额外开一个长为 S 的数组来存储计算出来的答案 F(S) 。<br />
<br />**代码：dp table，自下而上**<br />**(1)**
```python
class Solution:
    def coinChange(self, coins, amount):
        # 定义一维dp数组
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            # 这里从coin开始遍历
            for tmp_amount in range(coin, amount+1)
            	dp[tmp_amount] = min(dp[tmp_amount], dp[tmp_amount-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
```
**(2)遍历顺序不同：**
```python
class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf') _ in range(amount+1)]
        dp[0] = 0
        for tmp_amount in range(1, amount+1):
            for coin in coins:
                if tmp_amount >= coin:
                    dp[tmp_amount] = min(dp[tmp_amount], dp[tmp_amount-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1
```
感觉这种更好理解<br />**<br />**复杂度分析:**<br />**时间复杂度：O(Sn)**，其中 S 是金额，n 是面额数。我们一共需要计算 O(S) 个状态，S 为题目所给的总金额。对于每个状态，每次需要枚举 n 个面额来转移状态，所以一共需要 O(Sn) 的时间复杂度。<br />**空间复杂度：O(S)**。DP 数组需要开长度为总金额 S 的空间。<br />
<br />总结：这道题一个纯正的DP题，但是综合性很强，看了很多题解，可以用很多种解法，DFS，BFS，贪心，回溯，动态规划（dp table，记忆化搜索）。最后leetcode运行的时候，使用DFS+剪枝的方式是最快的，动态规划—dp table 自底向上 的效率要好于 动态规划-记忆化搜索。

这道题难点就是状态转移方程比较难写出，根据labuladong所讲的，要先找到状态，所谓的状态就是原问题和子问题中，都在变化的变量，放在这道题中，子问题和原问题一直在变化的变量是 amount，硬币数没有数量要求，所以不算，最后要推导出  dp[n] = min(dp[n], dp[n-coin]+1)

<a name="hnQ44"></a>
#### [不同路径](https://leetcode-cn.com/problems/unique-paths/)
**题解**：一个机器人位于一个 m x n 网格的左上角 。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角。问总共有多少条不同的路径？<br />
<br />这道题如果突然给我，我是不知道利用动态规划去求解的。但是如果指定好用动态规划去求解，那么这道题还是比较容易想的。<br />
<br />首先，这道题是包含重复子问题的，这里的子问题还是比较明显的，每一条路径都是由向右走，向下走组成的。<br />
<br />接下来就是动态规划中重要以及难点的问题，就是状态方程。看了很多题解的讲解，如果对状态方程不熟悉，不能直接写出的话，还是建议画图，进行推导以及找规律。 <br />
<br />确定状态方程的第一步，确定状态，在原问题以及子问题中，始终存在变化的是网格中，机器人上下左右坐标的变化，根据题解，机器人只能向右移动，已经向下移动。所以可以先写出 dp[i][j] 二维dp数组，我们令 `dp[i][j]` 是到达 `i, j` 最多路径，接下来用画图来表示状态方程之间的关系。<br />
<br />![截屏2020-07-15 下午9.25.58.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594819831643-6acb3ebc-7a7d-40cb-908a-4c69eb7acac8.png#align=left&display=inline&height=832&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-15%20%E4%B8%8B%E5%8D%889.25.58.png&originHeight=832&originWidth=820&size=68397&status=done&style=none&width=820)<br />
<br />上图是列举了4x4的网格，每个格子中的数字代表到达该点的路径数，我们以左上角的1 设为起点，i,j分别为0，0，所以表示为dp[0][0]，图中分别画出了起点到dp[1][1]，dp[1][2]的曲线，dp[1][1] = 2，dp[1][2] = 3

这里要注意 dp[1][?] ，dp[?][1] 全部为1，因为从起点到这一系列点，只能向右直走，或者向下直走，最多只有一条路径。

所以现在根据现有的值，我们可以发现：

> dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 =2
> dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3



所以这里总结出  动态方程：`dp[i][j] = dp[i-1][j] + dp[i][j-1]`<br />
<br />这里和杨辉三角相似，一个点的值，是由这个点的相邻左元素，相邻上元素之和构成的（边界点除外）<br />
<br />有了状态方程，接下来写程序<br />
<br />**代码：**
```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 定义dp二维数组
        dp = [[1]*n,[1]+[0]*(n-1) for _ in range(m-1)]
        # 起点为dp[0][0],所以没有m+1, n+1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```
复杂度：<br />时间复杂度：O(m*n)<br />空间复杂度：O(m*n)

为什么会有优化的空间呢，因为观察上面的代码，我们只要记录这两个数dp[i-1][j],dp[i][j-1]<br />**优化：滚动数组**<br />滚动数组思想是一种常见的动态规划优化方法，在题目中已经多次使用到，例如「剑指 Offer 46. 把数字翻译成字符串」、「70. 爬楼梯」等，当定义的状态在动态规划的转移方程中只和某几个状态相关的时候，就可以考虑这种优化方法，目的是给空间复杂度「降维」。

**代码优化一：**<br />用两个数组来维护状态，两个数组代表着上下相邻的两行。既然只有两行，则无所谓横坐标i，只是固定的j变换，得到结果。<br />![截屏2020-07-16 下午3.13.23.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594883657543-67b9bbc5-1d03-4bf3-a0e3-f2feda398be0.png#align=left&display=inline&height=222&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-16%20%E4%B8%8B%E5%8D%883.13.23.png&originHeight=222&originWidth=728&size=49861&status=done&style=none&width=728)
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]
```
空间复杂度 O(2n)<br />
<br />**代码优化二：**<br />用一个一维数组来优化，直接看代码很难理解一个一维数组是怎么实现的，但是只要把图画出来，就很巧妙，原理和优化一是一样的。只不过是用一个一维数组，很巧妙的存储了上下两个一维数组的值。 1111 1234 13610 这样一行一行的算，cur[j] = cur[j] + cur[j-1]，等号右边分别是该位置上边的值和左边的值<br />![截屏2020-07-16 下午5.05.58.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594890427325-d9b9e31e-9341-4df4-b74e-e51cf0ca48a7.png#align=left&display=inline&height=470&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-16%20%E4%B8%8B%E5%8D%885.05.58.png&originHeight=470&originWidth=612&size=50429&status=done&style=none&width=612)
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
```
空间复杂度 O(2n)<br />
<br />**总结分析：**<br />状态方程很难写出，但是通过画图可以直观的找到关联，写出状态方程。<br />写好状态方程后，看看是否能通过优化，来降低空间复杂度。<br />
<br />

<a name="BGz6S"></a>
#### [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)
题解：与[不同路径](https://leetcode-cn.com/problems/unique-paths/)不同的是，现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？<br />本题参数直接给出一个二维数组obstacleGrid: List[List[int]]，其中障碍物使用 1 来表示，其它则是0

此题和上一题思路一样，我开始想复杂了，以为多了一个障碍点，那么原来的状态方程可能就不能成立了。但是当你画完图，你会发现，其实还是一样的，只不过需要将障碍点设置为dp[i][j] == 0。

![截屏2020-07-16 下午7.55.36.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594900596100-e198812b-3c74-464f-8e60-4ceff08fed19.png#align=left&display=inline&height=332&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-16%20%E4%B8%8B%E5%8D%887.55.36.png&originHeight=332&originWidth=330&size=19161&status=done&style=none&width=330)<br />![截屏2020-07-16 下午7.56.38.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594900708722-e3a289d1-a8f7-4cee-bb36-c8f386bf344f.png#align=left&display=inline&height=844&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-16%20%E4%B8%8B%E5%8D%887.56.38.png&originHeight=844&originWidth=1562&size=190861&status=done&style=none&width=1562)<br />
<br />**代码：**
```python
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        :直接在原数组上进行路线的赋值
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                # 障碍点赋值
                if obstacleGrid[i][j]:
                    # 障碍点路线为0
                    obstacleGrid[i][j] = 0
                else:
                    if i == j == 0: obstacleGrid[i][j] = 1
                    else:
                        up = obstacleGrid[i-1][j] if i!=0 else 0
                        left = obstacleGrid[i][j-1] if j!=0 else 0
                        obstacleGrid[i][j] = up + left
        return obstacleGrid[-1][-1]
```

<br />**复杂度分析：**<br />**时间复杂度： **O(m*n)<br />**空间复杂度： **O(m*n) <br />**<br />**总结：**和不同路径一样~~ 只是这道题我是选择在原图上直接更改路线。<br />**
<a name="D5wtn"></a>
#### [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
**题解：**text1 = "abcde", text2 = "ace" ，最长公共子序列是 "ace"，它的长度为 3。<br />![截屏2020-07-17 下午3.26.18.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594970866550-bb19f0af-2142-4551-8174-a7807c17a830.png#align=left&display=inline&height=946&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-17%20%E4%B8%8B%E5%8D%883.26.18.png&originHeight=946&originWidth=1474&size=162208&status=done&style=none&width=1474)<br />**将两个字符串转化成二维数组：**<br />![截屏2020-07-17 下午4.32.36.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594974836784-e000dcac-3acb-4a7c-9fc6-d47f453149c3.png#align=left&display=inline&height=1164&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-17%20%E4%B8%8B%E5%8D%884.32.36.png&originHeight=1164&originWidth=1586&size=254219&status=done&style=none&width=1586)<br />**这个题解是我看过最简单的了。**<br />根据以上分析，得出状态转移方程：<br />![f25ddd4af8304e5aa9bb0c724fba79002e52831bbe203135f5ea715f41c92510-image.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1594974443267-b20a2771-e5db-4b3a-b1df-46cd8f60d8d9.png#align=left&display=inline&height=85&margin=%5Bobject%20Object%5D&name=f25ddd4af8304e5aa9bb0c724fba79002e52831bbe203135f5ea715f41c92510-image.png&originHeight=85&originWidth=577&size=24133&status=done&style=none&width=577)<br />
<br />**代码：**
```python
class Solution(object):
    def longestCommonSubsequence(self, str_1, str2):
        m, n = len(str_1), len(str2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str_1[i - 1] == str2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
```
**复杂度分析：**<br />时间复杂度：O(m * n)，其中 m 和 n 分别为 A 和 B 的 长度。<br />空间复杂度：O(m * n)，其中 m 和 n 分别为 A 和 B 的 长度。<br />
<br />**总结：这题的难点是需要从字符串，转化成二维数组。而路径题或零钱兑换都有明显的一维二维结构。这里还有一点需要注意，就是要多实例化一行与一列，dp[0][x] dp[x][0] 代表空子串。**<br />**<br />**
<a name="t25Jg"></a>
#### [三角形最小路径和](https://leetcode-cn.com/problems/triangle/)
**题解：**给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。<br />例如，给定三角形：<br />triangle = [<br />     [2],<br />    [3,4],<br />   [6,5,7],<br />  [4,1,8,3]<br />]<br />
<br />典型的动态规划题目，求最值。<br />这里我有想到过肯定是用二维数组，但是我要不要将给定的数组进行补零呢~~~，但是好像并不用，因为每个子数组都是从下标0开始的。<br />
<br />**算法：**

1. 寻找子问题：

我们把目光聚焦在相邻的[2]和[3, 4]中，不要去看其它行，解决这个子问题就好。那么这两个相邻的行，怎么求解最小路径和呢？？？其实很容易写出，但是需要注意数组的坐标<br />problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + triangle[i, j]

2.  定义状态数组 ：dp[i][j]
2.  状态方程： dp[i][j] = min(dp(i+1, j), dp(i+1, j+1)) + triangle[i, j]

**<br />**代码：**
```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        # 直接在原数组上进行操作
        # down_to_up, 从倒数第二层开始，因为计算每i层时，会和i+1层进行计算
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
```
**<br />**复杂度分析：**<br />时间复杂度：O(N^2)，N 为三角形的行数。<br />空间复杂度：O(N^2)，N 为三角形的行数。

**优化：**<br />还是down_to_up，初始化一个一维数组，先将最后一行拿出来
```python
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle: return 0
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j] + res[j+1]) + triangle[i][j]
        return res[0]
```
时间复杂度：O(N^2)，N 为三角形的行数。<br />空间复杂度：O(N)，N为三角形的行数。<br />**<br />**总结：**<br />这题我是没有想清楚要自上至下，还是自下至上。后来发现还是自下至上要简单一些，自上至下要判断一些边界条件。<br />[高票解答](https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up))<br />**<br />**
<a name="0fjqc"></a>
#### [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
**题解：**给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。示例:输入: [-2,1,-3,4,-1,2,1,-5,4], 输出: 6解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

1. dp方程： dp[i] = max(nums[i], nums[i]+dp[i-1]) 
1. 其实就是  **最大子序列和 =  当前自身最大，还是当前自身+前面子序列和最大**

**代码：**
```python
class Solution(object):
    """原数组操作""""
    def maxSubArray(self, nums):
        if not nums: return None
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)
```
定义dp
```python
class Solution(object):
    def maxSubArray(self, nums):
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])
        return max(dp)
```
复杂度分析：<br />以上两种写法的复杂度：<br />**时间复杂度 O(n)、空间复杂度 O(n)**<br />**<br />我们可以只用一个变量 pre 来维护对于当前 f(i) 的 f(i - 1)的值是多少，从而让空间复杂度降低到 O(1)，这有点类似「滚动数组」的思想。
```python
class Solution(object):
    def maxSubArray(self, nums):
        pre = 0
        max_sum = nums[0]
        for num in nums:
            # 保存当前最大路径
            pre = max(pre+num, num)
            # 借助max_sum来保存最大和
            max_sum = max(max_sum, pre)
        return max_sum
```
**<br />**复杂度分析：**<br />时间复杂度：O(n)，其中 n 为 nums 数组的长度。我们只需要遍历一遍数组即可求得答案。<br />空间复杂度：O(1)。我们只需要常数空间存放若干变量。<br />
<br />**总结：**<br />**<br />**
<a name="VkPtT"></a>
#### [打家劫舍](https://leetcode-cn.com/problems/house-robber/)
**题解：**你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。<br />给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。<br />示例 1：<br />输入：[1,2,3,1]<br />输出：4<br />解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。<br />     偷窃到的最高金额 = 1 + 3 = 4 。<br />
<br />动态规划的的四个解题步骤是：

- 定义子问题

子问题就是“从 k 个房子中能偷到的最大金额”，用 f(k) 表示。

- 写出子问题的递推关系

![截屏2020-07-18 下午11.47.32.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1595087445565-9d5452c7-e882-4979-b2c4-e34b90ccd5fe.png#align=left&display=inline&height=822&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-18%20%E4%B8%8B%E5%8D%8811.47.32.png&originHeight=822&originWidth=1570&size=239297&status=done&style=none&width=1570)

- 确定 DP 数组的计算顺序

**自上向下的递归备忘录方法和自下向上的dp数组循环法，99%的情况使用自下向上的dp数组循环法就可以**

- 空间优化（可选）


<br />**代码：**
```python
class Solution(object):
    def rob(self, nums):
        if not nums: return 0
        size = len(nums)
        # 边界条件
        if size == 1: return nums[0]
        # 定义dp数组
        dp = [0] * size
        # 初始化, 分别为一间房和两间房的情况
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # dp[0]代表起始元素，则size不用加一
        for i in range(2, size):
            # 分别是：最后一间房没有抢， 最后一间房抢了。
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

```
复杂度分析<br />**时间复杂度**：O(n)，其中 n 是数组长度。只需要对数组遍历一次。<br />**空间复杂度**：O(n)

**空间优化版本**<br />**<br />空间优化的基本原理是，很多时候我们并不需要始终持有全部的 DP 数组。对于小偷问题，我们发现，最后一步计算 f(n) 的时候，实际上只用到了 f(n−1) 和 f(n−2) 的结果。n-3 之前的子问题，实际上早就已经用不到了。那么，我们可以只用两个变量保存两个子问题的结果，就可以依次计算出所有的子问题。下面的动图比较了空间优化前和优化后的对比关系：<br />**![3dcbb1028ed9cdac95fdc8c8348ccc6f2e4c50b3fd8222e5690257d6b495090a.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1595088226615-9cd228cb-46c9-40f2-ac39-3f3d2b90c1f8.gif#align=left&display=inline&height=500&margin=%5Bobject%20Object%5D&name=3dcbb1028ed9cdac95fdc8c8348ccc6f2e4c50b3fd8222e5690257d6b495090a.gif&originHeight=500&originWidth=1200&size=282364&status=done&style=none&width=1200)**
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        # 每次循环，计算当前房子为止的最大金额值
        for num in nums:
            # cur 为 dp[i-1], pre = dp[i-2]
            cur, pre = max(pre + num, cur), cur
            # cur = dp[i], pre = dp[i-1]
        return cur
```
**复杂度分析：**<br />
<br />时间复杂度：O(n)，其中 n 是数组长度。只需要对数组遍历一次。<br />空间复杂度：O(1)。使用滚动数组，可以只存储前两间房屋的最高总金额，而不需要存储整个数组的结果，因此空间复杂度是 O(1)。<br />**<br />**总结：**<br />
<br />动态规划的的四个解题步骤是：

- 定义子问题

子问题就是“从 k 个房子中能偷到的最大金额”，用 f(k) 表示。

- 写出子问题的递推关系
- 确定 DP 数组的计算顺序

**自上向下的递归备忘录方法和自下向上的dp数组循环法，99%的情况使用自下向上的dp数组循环法就可以**

- 空间优化（可选）**

**<br />**题解：**<br />**代码：**<br />**复杂度分析：**<br />**总结：**

---

**
<a name="NJ5YL"></a>
### 总结
**<br />**模板**<br />**自底向上dp数组法**
```python
class solution:
    def userDefineFunction(self, nums or List[List[int]]):
        # 边界条件
        if not nums: return
        # 创建dp数组，根据题目，判断创建一维或者是二维dp数组
        # 一维 
        dp = [0 or float('-inf')] * len(nums) or len(nums)+1
        # 二维
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        
        # 初始化 有时可能需要对dp[0], dp[1]进行初始化
        dp[0] = 0
        
        for i in range(len(nums))
        or 
        for i in range(1, len(list)):
        	for h in range(len(list[0])):
                # ！！！dp方程！！！
                dp[i][j] = dp..............
        return dp[-1]
```
**对于有些可以进行空间优化的，一般都是当前状态只和前面一个或两个状态有关系的时候。**
```python
class solution:
    def userDefineFunction(self, nums or List[List[int]]):
        pre, cur = ...
        for num in nums:
            change(cur, pre)
            # eg:cur, pre = max(..), cur
        return cur
```
**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**<br />**
