# coding: utf-8
# Author：Brent
# Date ：2020/7/18 11:39 AM
# Tool ：PyCharm
# Describe ：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
class Solution(object):

    def maxSubArray(self, nums):
        """原数组上进行操作"""
        if not nums: return None
        for i in range(1, len(nums)):
           nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)

    def maxSubArray_1(self, nums):
        """dp"""
        if not nums: return None
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)

    def maxSubArray_2(self, nums):
        """O（1）"""
        pre = 0
        max_sum = nums[0]
        for num in nums:
            pre = max(pre+num, num)
            max_sum = max(max_sum, pre)
        return max_sum




if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray_1(nums))