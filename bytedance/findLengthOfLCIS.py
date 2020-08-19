# coding: utf-8
# Author：Brent
# Date ：2020/8/18 4:09 PM
# Tool ：PyCharm
# Describe ：
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5,4,2,3,4,5]
    print(solution.findLengthOfLCIS(nums))