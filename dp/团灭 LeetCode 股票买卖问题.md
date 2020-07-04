<a name="JJDTz"></a>
### 思路介绍
很多读者抱怨 LeetCode 的股票系列问题奇技淫巧太多，如果面试真的遇到这类问题，基本不会想到那些巧妙的办法，怎么办？**所以本文拒绝奇技淫巧，而是稳扎稳打，只用一种通用方法解决所用问题，以不变应万变**。<br />这篇文章用状态机的技巧来解决，可以全部提交通过。不要觉得这个名词高大上，文学词汇而已，实际上就是 DP table，看一眼就明白了。<br />
<br />PS：本文参考自[英文版 LeetCode 的一篇题解](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038)。<br />
<br />先随便抽出一道题，看看别人的解法：<br />

```python
int maxProfit(vector<int>& prices) {
    if(prices.empty()) return 0;
    int s1=-prices[0],s2=INT_MIN,s3=INT_MIN,s4=INT_MIN;
        
    for(int i=1;i<prices.size();++i) {            
        s1 = max(s1, -prices[i]);
        s2 = max(s2, s1+prices[i]);
        s3 = max(s3, s2-prices[i]);
        s4 = max(s4, s3+prices[i]);
    }
    return max(0,s4);
}
```
能看懂吧？会做了吗？不可能的，你看不懂，这才正常。就算你勉强看懂了，下一个问题你还是做不出来。为什么别人能写出这么诡异却又高效的解法呢？因为这类问题是有框架的，但是人家不会告诉你的，因为一旦告诉你，你五分钟就学会了，该算法题就不再神秘，变得不堪一击了。<br />
<br />本文就来告诉你这个框架，然后带着你一道一道秒杀。这篇文章用状态机的技巧来解决，可以全部提交通过。不要觉得这个名词高大上，文学词汇而已，实际上就是 DP table，看一眼就明白了。<br />这 6 道题目是有共性的，我就抽出来第 4 道题目，因为这道题是一个最泛化的形式，其他的问题都是这个形式的简化，看下题目：<br />[![](https://github.com/labuladong/fucking-algorithm/raw/master/pictures/%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98/title.png#align=left&display=inline&height=622&margin=%5Bobject%20Object%5D&originHeight=622&originWidth=798&status=done&style=none&width=798)](https://github.com/labuladong/fucking-algorithm/blob/master/pictures/%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98/title.png)<br />
<br />第一题是只进行一次交易，相当于 k = 1；<br />第二题是不限交易次数，相当于 k = +infinity（正无穷）；<br />第三题是只进行 2 次交易，相当于 k = 2；<br />剩下两道也是不限次数，但是加了交易「冷冻期」和「手续费」的额外条件，其实就是第二题的变种，都很容易处理。<br />

<a name="KEGVj"></a>
#### 一、穷举框架
首先，还是一样的思路：如何穷举？这里的穷举思路和上篇文章递归的思想不太一样。<br />递归其实是符合我们思考的逻辑的，一步步推进，遇到无法解决的就丢给递归，一不小心就做出来了，可读性还很好。缺点就是一旦出错，你也不容易找到错误出现的原因。比如上篇文章的递归解法，肯定还有计算冗余，但确实不容易找到。<br />
<br />而这里，我们不用递归思想进行穷举，而是利用「状态」进行穷举。我们具体到每一天，看看总共有几种可能的「状态」，再找出每个「状态」对应的「选择」。我们要穷举所有「状态」，穷举的目的是根据对应的「选择」更新状态。听起来抽象，你只要记住「状态」和「选择」两个词就行，下面实操一下就很容易明白了。<br />
```python
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
```
比如说这个问题，**每天都有三种「选择」**：买入、卖出、无操作，我们用 buy, sell, rest 表示这三种选择。<br />
<br />但问题是，并不是每天都可以任意选择这三种选择的，因为 sell 必须在 buy 之后，buy 必须在 sell 之后。那么 rest 操作还应该分两种状态，一种是 buy 之后的 rest（持有了股票），一种是 sell 之后的 rest（没有持有股票）。<br />
<br />而且别忘了，我们还有交易次数 k 的限制，就是说你 buy 还只能在 k > 0 的前提下操作。<br />
<br />很复杂对吧，不要怕，我们现在的目的只是穷举，你有再多的状态，老夫要做的就是一把梭全部列举出来。**这个问题的「状态」有三个**，第一个是天数，第二个是允许交易的最大次数，第三个是当前的持有状态（即之前说的 rest 的状态，我们不妨用 1 表示持有，0 表示没有持有）。然后我们用一个三维数组就可以装下这几种状态的全部组合：<br />

```python
dp[i][k][0 or 1]
0 <= i <= n-1, 1 <= k <= K
n 为天数，大 K 为最多交易数
此问题共 n × K × 2 种状态，全部穷举就能搞定。
for i in range(n):
    for k in range(1,K+1):
        for s in {0, 1}:
            dp[i][k][s] = max(buy, sell, rest)
```

<br />而且我们可以用自然语言描述出每一个状态的含义，比如说 `dp[3][2][1]` 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易。再比如 `dp[2][3][0]` 的含义：今天是第二天，我现在手上没有持有股票，至今最多进行 3 次交易。很容易理解，对吧？<br />
<br />我们想求的最终答案是 dp[n - 1][K][0]，即最后一天，最多允许 K 次交易，最多获得多少利润。读者可能问为什么不是 dp[n - 1][K][1]？因为 [1] 代表手上还持有股票，[0] 表示手上的股票已经卖出去了，很显然后者得到的利润一定大于前者。<br />
<br />记住如何解释「状态」，一旦你觉得哪里不好理解，把它翻译成自然语言就容易理解了。
<a name="6pIbJ"></a>
#### 
<a name="4aY7l"></a>
#### 二、状态转移框架
现在，我们完成了「状态」的穷举，我们开始思考每种「状态」有哪些「选择」，应该如何更新「状态」。只看「持有状态」，可以画个状态转移图。<br />[![](https://github.com/labuladong/fucking-algorithm/raw/master/pictures/%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98/1.png#align=left&display=inline&height=519&margin=%5Bobject%20Object%5D&originHeight=519&originWidth=794&status=done&style=none&width=794)](https://github.com/labuladong/fucking-algorithm/blob/master/pictures/%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98/1.png)<br />通过这个图可以很清楚地看到，每种状态（0 和 1）是如何转移而来的。根据这个图，我们来写一下状态转移方程：
```python
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              #￥max(   选择 rest  ,             选择 sell      )

```
解释：今天我没有持有股票，有两种可能：<br />要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；<br />要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。
```python
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
              #max(   选择 rest  ,           选择 buy         )
```
解释：今天我持有着股票，有两种可能：<br />要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；<br />要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。<br />
<br />这个解释应该很清楚了，如果 buy，就要从利润中减去 prices[i]，如果 sell，就要给利润增加 prices[i]。今天的最大利润就是这两种可能选择中较大的那个。**而且注意 k 的限制和变化，根据题意，****允许完成一笔交易（即买入和卖出一支股票一次），****我们在选择 buy 的时候，把 k 减小了 1，所以在卖出的时候就不用减小1了，很好理解吧，当然你也可以在 sell 的时候减 1，一样的。**<br />**<br />现在，我们已经完成了动态规划中最困难的一步：状态转移方程。如果之前的内容你都可以理解，那么你已经可以秒杀所有问题了，只要套这个框架就行了。不过还差最后一点点，就是定义 base case，即最简单的情况。
```python
dp[-1][k][0] = 0
解释：因为 i 是从 0 开始的，所以 i = -1 意味着还没有开始，这时候的利润当然是 0 。
dp[-1][k][1] = -infinity
解释：还没开始的时候，是不可能持有股票的，用负无穷表示这种不可能。
dp[i][0][0] = 0
解释：因为 k 是从 1 开始的，所以 k = 0 意味着根本不允许交易，这时候利润当然是 0 。
dp[i][0][1] = -infinity
解释：不允许交易的情况下，是不可能持有股票的，用负无穷表示这种不可能。
```

<br />把上面的状态转移方程总结一下：
```python
base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity
状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
读者可能会问，这个数组索引是 -1 怎么编程表示出来呢，负无穷怎么表示呢？这都是细节问题，有很多方法实现。现在完整的框架已经完成，下面开始具体化。<br />
<br />**以上是labuladong讲解的状态方程变化，我觉得讲的很不错，至少我从不知道状态方程是什么，到已经理解了。**<br />**下面的题解部分，我有修改成python，并且根据自己能更好理解的方式进行了修改，labuladong的题解是采用了空间复杂度O(1)的方法，使用固定的两个变量来转换。而我下面的方式是dp[i][0]这种方式，这种方式我写的时候思路更清晰。但是这种方式的空间复杂度貌似是O(n)的。**

---

<a name="GVn6V"></a>
#### 三、秒杀题目
**第一题，k = 1**<br />直接套状态转移方程，根据 base case，可以做一些化简：
```
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
						= max(dp[i-1][1][1], -prices[i])
```
解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。<br />现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。<br />可以进行进一步化简去掉所有 k：
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])
```

<br />直接写出代码：
```python
    n = len(prices)
    dp = [[]]
    for i in range(n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n - 1][0]
```

<br />显然 i = 0 时 dp[i-1] 是不合法的。这是因为我们没有对 i 的 base case 进行处理。可以这样处理：
```python
    for i in range(n):
        if i - 1 == -1:
            dp[i][0] = 0;
            # 解释：
            #   dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i])
            #            = max(0, -infinity + prices[i]) = 0
            dp[i][1] = -prices[i]
            #解释：
            #   dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i])
            #            = max(-infinity, 0 - prices[i]) 
            #            = -prices[i]
            continue

        dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = Math.max(dp[i-1][1], -prices[i])

    return dp[n - 1][0]
```
第一题就解决了，但是这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):<br />

```python
// k == 1
def maxProfit(self, prices):
    n = len(prices)
    // base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    dp_i_0 = 0
    dp_i_1 = float('-inf');
    for (int i = 0; i < n; i++) {
        // dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp_i_0 = Math.max(dp_i_0, dp_i_1 + prices[i]);
        // dp[i][1] = max(dp[i-1][1], -prices[i])
        dp_i_1 = Math.max(dp_i_1, -prices[i]);
    
    return dp_i_0;

```

<br />两种方式都是一样的，不过这种编程方法简洁很多。但是如果没有前面状态转移方程的引导，是肯定看不懂的。后续的题目，我主要写这种空间复杂度 O(1) 的解法。<br />
<br />没有使用变量的python代码：
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
**<br />**第二题，k = +infinity**<br />每天都有三种动作：买入（buy）、卖出（sell）、无操作（rest）。<br />因为不限制交易次数，因此交易次数这个因素不影响题目，不必考虑。DP Table 是二维的，两个维度分别是天数（0,1,...,n-1）和是否持有股票（1 表持有，0 表不持有）。<br />
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

<br />**第三题，k = +infinity with cooldown**<br />题解：<br />这道题的在 [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) 的基础上添加了冷冻期的要求，即每次 sell 之后要等一天才能继续交易。状态转移方程要做修改，如果第 i 天选择买入股票，状态要从第 i-2 的转移，而不是 i-1 (因为第 i-1 天是冷冻期)。另外，由于状态转移方程中出现了 dp[i-2] 推导 dp[i-1]，因此状态边界除了考虑 i=0 天，**还要加上 i=1 天的状态。**Solution 如下<br />
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
**第四题，k = +infinity with fee**<br />每次交易要支付手续费，只要把手续费从利润中减去即可。改写方程：
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
解释：相当于买入股票的价格升高了。
在第一个式子里减也是一样的，相当于卖出股票的价格减小了。
```
直接翻译成代码：
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
**第五题，k = 2**<br />题目约定最多交易次数 k=2，因此交易次数必须作为一个新的维度考虑进 DP Table 里，也就是说，这道题需要三维 DP 来解决。三个维度分别为：天数 i（i=0,1,...,n-1），买入股票的次数 j（j=1,2,...,k）和是否持有股票（1 表持有，0 表不持有）. 特别注意买入股票的次数为 j 时，其实隐含了另一个信息，就是卖出股票的次数为 j-1 或 j 次。<br />
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

<br />**<br />**第六题，k = any integer**<br />有了上一题 k = 2 的铺垫，这题应该和上一题的第一个解法没啥区别。但是出现了一个超内存的错误，原来是传入的 k 值会非常大，dp 数组太大了。现在想想，交易次数 k 最多有多大呢？<br />
<br />一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。这种情况是之前解决过的。<br />直接把之前的代码重用：
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
至此，6 道题目通过一个状态转移方程全部解决。<br />**四、最后总结**<br />本文给大家讲了如何通过状态转移的方法解决复杂的问题，用一个状态转移方程秒杀了 6 道股票买卖问题，现在想想，其实也不算难对吧？这已经属于动态规划问题中较困难的了。<br />关键就在于列举出所有可能的「状态」，然后想想怎么穷举更新这些「状态」。一般用一个多维 dp 数组储存这些状态，从 base case 开始向后推进，推进到最后的状态，就是我们想要的答案。想想这个过程，你是不是有点理解「动态规划」这个名词的意义了呢？<br />具体到股票买卖问题，我们发现了三个状态，使用了一个三维数组，无非还是穷举 + 更新，不过我们可以说的高大上一点，这叫「三维 DP」，怕不怕？这个大实话一说，立刻显得你高人一等，名利双收有没有，所以给个在看/分享吧，鼓励一下我。<br />**致力于把算法讲清楚！欢迎关注我的微信公众号 labuladong，查看更多通俗易懂的文章**：<br />[![](https://github.com/labuladong/fucking-algorithm/raw/master/pictures/labuladong.png#align=left&display=inline&height=591&margin=%5Bobject%20Object%5D&originHeight=591&originWidth=1772&status=done&style=none&width=1772)](https://github.com/labuladong/fucking-algorithm/blob/master/pictures/labuladong.png) [Hanmin](https://github.com/Miraclemin/) 提供 Python3 代码:<br />**第一题，k = 1**<br />def maxProfit(self, prices: List[int]) -> int:<br />    dp_i_0,dp_i_1 = 0,float('-inf')<br />    for price in prices:<br />        dp_i_0 = max(dp_i_0, dp_i_1 + price)<br />        dp_i_1 = max(dp_i_1, -price)<br />    return dp_i_0<br />**第二题，k = +infinity**<br />def maxProfit_k_inf(self, prices: List[int]) -> int:<br />    dp_i_0,dp_i_1 = 0,float('-inf')<br />    for price in prices:<br />        temp = dp_i_0<br />        dp_i_0 = max(dp_i_0, dp_i_1 + price)<br />        dp_i_1 = max(dp_i_1, temp - price)<br />    return dp_i_0<br />**第三题，k = +infinity with cooldown**<br />def maxProfit_with_cool(self, prices: List[int]) -> int:<br />    dp_i_0,dp_i_1 = 0,float('-inf')<br />    dp_pre_0 = 0 ##代表 dp[i-2][0]<br />    for price in prices:<br />        temp = dp_i_0<br />        dp_i_0 = max(dp_i_0, dp_i_1 + price)<br />        dp_i_1 = max(dp_i_1, dp_pre_0 - price)<br />        dp_pre_0 = temp<br />    return dp_i_0<br />**第四题，k = +infinity with fee**<br />def maxProfit_with_fee(self, prices: List[int], fee: int) -> int:<br />    dp_i_0,dp_i_1 = 0,float('-inf')<br />    for price in prices:<br />        temp = dp_i_0<br />        dp_i_0 = max(dp_i_0, dp_i_1 + price)<br />        dp_i_1 = max(dp_i_1, temp - price -fee)<br />    return dp_i_0<br />**第五题，k = 2**<br />def maxProfit_k_2(self, prices: List[int]) -> int:<br />    dp_i10,dp_i11 = 0,float('-inf')<br />    dp_i20,dp_i21 = 0,float('-inf')<br />    for price in prices:<br />        dp_i20 = max(dp_i20, dp_i21 + price)<br />        dp_i21 = max(dp_i21, dp_i10 - price)<br />        dp_i10 = max(dp_i10, dp_i11 + price)<br />        dp_i11 = max(dp_i11, -price)<br />    return dp_i20<br />**第六题，k = any integer**<br />def maxProfit_k_any(self, max_k: int, prices: List[int]) -> int:<br />    n = len(prices)<br />    if max_k > n // 2:<br />        return self.maxProfit_k_inf(prices)<br />    else:<br />        dp = [[[None, None] for _ in range(max_k + 1)] for _ in range(n)]<br />        for i in range(0,n):<br />            for k in range(max_k,0,-1):<br />                if i-1 == -1:## 处理 base case<br />                    dp[i][k][0] = 0<br />                    ## 解释：<br />                    ## dp[i][k][0] = max(dp[-1][k][0], dp[-1][k][1] + prices[i])<br />                    ## = max(0, -infinity + prices[i]) = 0<br />                    dp[i][k][1] = -prices[i]<br />                    ## 解释：<br />                    ## dp[i][1] = max(dp[-1][k][1], dp[-1][k][0] - prices[i])<br />                    ## = max(-infinity, 0 - prices[i]) = -prices[i]<br />                    continue<br />                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])<br />                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])<br />        return dp[n - 1][max_k][0];<br />

