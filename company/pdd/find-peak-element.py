# coding: utf-8
# Author：Brent
# Date ：2020/9/18 12:53 AM
# Tool ：PyCharm
# Describe ：峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。


class Solution:
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if mid == len(nums) - 1:
                return mid
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 5, 6, 4]
    solution = Solution()
    solution.findPeakElement(nums)