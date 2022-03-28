# coding: utf-8
# Author：Brent
# Date ：2020/8/2 12:00 PM
# Tool ：PyCharm
# Describe ：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for fast_index in range(len(nums)):
            if nums[fast_index] != 0:
                nums[zero_index], nums[fast_index] = nums[fast_index], nums[zero_index]
                zero_index += 1
        return nums

    def moveZeroesII(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        return nums


if __name__ == '__main__':
    nums = [0, 0, 1, 0, 3, 12]
    solution = Solution()
    print(solution.moveZeroes(nums))
