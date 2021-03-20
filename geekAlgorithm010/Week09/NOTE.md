

**动态规划复习**<br />
![截屏2020-08-06 上午9.14.51.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676545984-86a19ec7-b11b-4960-af7c-5a160238d910.png#align=left&display=inline&height=1222&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.14.51.png&originHeight=1222&originWidth=1612&size=265654&status=done&style=none&width=1612)![截屏2020-08-06 上午9.15.01.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676547120-064ee8c2-b2bd-4bc0-b06f-6d432fe88291.png#align=left&display=inline&height=1196&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.01.png&originHeight=1196&originWidth=1574&size=222445&status=done&style=none&width=1574)![截屏2020-08-06 上午9.15.11.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676548127-28b68019-cce0-489c-84c4-87544140db15.png#align=left&display=inline&height=756&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.11.png&originHeight=756&originWidth=1588&size=157797&status=done&style=none&width=1588)![截屏2020-08-06 上午9.15.24.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676549117-38ad8f49-f7e1-4383-9230-ae72152990b2.png#align=left&display=inline&height=944&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.24.png&originHeight=944&originWidth=1586&size=206461&status=done&style=none&width=1586)<br />![截屏2020-08-06 上午9.14.51.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676859655-34abb93f-c3d6-45d3-b821-d570483b682a.png#align=left&display=inline&height=1222&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.14.51.png&originHeight=1222&originWidth=1612&size=265654&status=done&style=none&width=1612)![截屏2020-08-06 上午9.15.01.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676860673-72f79590-6756-49d5-b8a0-43eae8eb4923.png#align=left&display=inline&height=1196&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.01.png&originHeight=1196&originWidth=1574&size=222445&status=done&style=none&width=1574)![截屏2020-08-06 上午9.15.11.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676861948-57a2de0e-06f1-4115-b758-643e10bbc9ca.png#align=left&display=inline&height=756&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.11.png&originHeight=756&originWidth=1588&size=157797&status=done&style=none&width=1588)![截屏2020-08-06 上午9.15.24.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596676863052-396b0ebf-a8a3-4e16-899c-913635623b7d.png#align=left&display=inline&height=944&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-06%20%E4%B8%8A%E5%8D%889.15.24.png&originHeight=944&originWidth=1586&size=206461&status=done&style=none&width=1586)
<a name="gnpRN"></a>
#### [使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)

<br />**首先要说明一下，这道题的题目描述跟屎一样~~~**<br />数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。<br />每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。<br />您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。<br />示例 1:<br />输入: cost = [10, 15, 20]<br />输出: 15<br />解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。<br />
<br />这里需要注意，需要求到底楼层顶部的最低花费，给的数组中，最后一个元素并不是楼顶，而是最靠近楼顶的台阶。这里可以在最后添加一个元素0，代表楼顶。<br />

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        # 防止越界，设置楼顶为0花费
        cost.append(0)
        # 定义状态数组
        dp = [0] * len(cost)
        # 初始化
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            # 和爬楼梯相似，i级台阶是从 i-1一步上来的  或者  i-2 两步上来的。
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return dp[-1]

    def minCostClimbingStairs_1(self, cost):
        # 防止越界，设置楼顶为0花费
        cost.append(0)
        a = cost[0]
        b = cost[1]

        for i in range(2, len(cost)):
            c = min(b + cost[i], a + cost[i])
            a, b = b, c
        return c
```
复杂度分析：<br />时间：O(n)<br />空间：O(1)<br />
<br />

<a name="c4d17298"></a>
#### [最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
给定一个无序的整数数组，找到其中最长上升子序列的长度。<br />示例:输入: [10,9,2,5,3,7,101,18]   输出: 4 <br />解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。<br />说明:可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。你算法的时间复杂度应该为 O(n2) 。<br />进阶: 你能将算法的时间复杂度降低到 O(nlogn) 吗?<br />
<br />题解：此题很容易想到动态规划求解，但是进阶部分要求将时间复杂度降低为 O(nlogn)，这看起来就是要引入某种O(nlogn)的排序算法，我是根本就想不出来的~~~~~~~~~~~~~~~~~~~~~~~~~

**动态规划**<br />**![截屏2020-08-07 上午10.01.51.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596765728963-d9decbf3-d3e2-4068-a3fa-863b39c716d5.png#align=left&display=inline&height=1136&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-07%20%E4%B8%8A%E5%8D%8810.01.51.png&originHeight=1136&originWidth=1672&size=267879&status=done&style=none&width=1672)**
```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
```

<br />**贪心+二分法**<br />**![截屏2020-08-07 上午10.33.30.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596767670747-57a557df-f34d-4ad9-9d89-33f7e2eedfc6.png#align=left&display=inline&height=1154&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-07%20%E4%B8%8A%E5%8D%8810.33.30.png&originHeight=1154&originWidth=1656&size=268778&status=done&style=none&width=1656)![截屏2020-08-07 上午10.33.47.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596767673298-93be11d2-ef30-4501-a328-a34e03b5df02.png#align=left&display=inline&height=802&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-07%20%E4%B8%8A%E5%8D%8810.33.47.png&originHeight=802&originWidth=1622&size=175229&status=done&style=none&width=1622)![截屏2020-08-07 上午10.33.57.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596767676670-cb89c0fe-8396-4cd4-9395-f52a698f4de7.png#align=left&display=inline&height=1180&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-07%20%E4%B8%8A%E5%8D%8810.33.57.png&originHeight=1180&originWidth=1636&size=343225&status=done&style=none&width=1636)![截屏2020-08-07 上午10.34.05.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596767678184-ed8ea508-e657-4ea6-9f5f-a07ecaaf3cf4.png#align=left&display=inline&height=548&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-08-07%20%E4%B8%8A%E5%8D%8810.34.05.png&originHeight=548&originWidth=1638&size=107859&status=done&style=none&width=1638)**
```python
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        # 特判
        if size < 2:
            return size

        # 为了防止后序逻辑发生数组索引越界，先把第 1 个数放进去
        tail = [nums[0]]
        for i in range(1, size):
            # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大
            # 先尝试是否可以接在末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            # 使用二分查找法，在有序数组 tail 中
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
                # mid = left + (right - left) // 2
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    # 中位数肯定不是要找的数，把它写在分支的前面
                    left = mid + 1
                else:
                    right = mid
            # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，
            # 因此无需再单独判断
            tail[left] = nums[i]
        return len(tail)
```
复杂度分析：<br />时间复杂度 O(NlogN) ： 遍历 nums 列表需 O(N)，在每个 nums[i] 二分法需 O(logN)。<br />空间复杂度 O(N) ： tails 列表占用线性大小额外空间。<br />
<br />

<a name="BgHiw"></a>
#### [转换成小写字母](https://leetcode-cn.com/problems/to-lower-case/)
```python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for char in str:
            if char >= 'A' and char <= 'Z':
                char = chr(ord(char) + 32)
            res+=char
        return res
```


<a name="ETWIG"></a>
#### [最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word/)
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        if not s or s == ' ': return 0
        last_word_len = 0
        last_space_flag = True
        for i in range(len(s)-1, -1,-1):
            if s[i] == ' ':
                if not last_space_flag:
                    break
                continue
            last_word_len+=1
            last_space_flag = False
        return last_word_len
```


<a name="t5jRc"></a>
#### [宝石与石头](https://leetcode-cn.com/problems/jewels-and-stones/)
```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        if not J or not S: return 0
        stone_dict = collections.defaultdict(int)
        count = 0
        for char in S:
            stone_dict[char] += 1
        for char in J:
            if char in stone_dict:
                count += stone_dict[char]
        return count
```

<br />复杂度分析<br />时间复杂度：O(J.length + S.length))  O(J.length}) 这部分来自于创建 J，O(S.length) 这部分来自于搜索 S。<br />空间复杂度：O(J.length)<br />

<a name="3wmOy"></a>
#### [最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)
此题使用纵向比较。还有其他解题方法：横向比较，二分法，分治法，利用字典法
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        for i in range(len(strs[0])):
            common_char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != common_char:
                    return strs[0][:i]
        return strs[0]

```

<br />复杂度分析<br />时间复杂度：O(mn)，其中 mm 是字符串数组中的字符串的平均长度，nn 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。<br />空间复杂度：O(1)。使用的额外空间复杂度为常数。<br />

<a name="8wBkB"></a>
#### [反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)
```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
```
复杂度分析<br />时间复杂度：O(N)，其中 N 是 s 的大小。我们建立一个辅助数组，用来翻转 s 的一半字符。<br />空间复杂度：O(N)，a 的大小。
