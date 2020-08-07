# coding: utf-8
# Author：Brent
# Date ：2020/8/6 11:21 AM
# Tool ：PyCharm
# Describe ：给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

# Dynamic programming.
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_1(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i + j) // 2
                if tails[mid] < num:
                    i = mid + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = mid
            tails[i] = num
            if j == res: res += 1
        return res


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    solution = Solution()
    res = solution.lengthOfLIS_1(nums)
    print(res)
