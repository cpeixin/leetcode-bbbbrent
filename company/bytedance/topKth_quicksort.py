# coding: utf-8
# Author：Brent
# Date ：2020/8/19 8:55 AM
# Tool ：PyCharm
# Describe ：
import random
from typing import List


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        target_index = len(nums) - k
        while True:
            index = self.partition(left, right, nums)
            if target_index == index:
                return nums[index]
            elif target_index > index:
                left = index + 1
            else:
                right = index - 1

    def partition(self, left, right, nums):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]
        pivot = nums[left]
        mark = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[left], nums[mark] = nums[mark], nums[left]
        return mark

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    solution.findKthLargest(nums, k)