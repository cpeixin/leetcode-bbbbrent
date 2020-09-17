# coding: utf-8
# Author：Brent
# Date ：2020/9/18 12:53 AM
# Tool ：PyCharm
# Describe ：

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