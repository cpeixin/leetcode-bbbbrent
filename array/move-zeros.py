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
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index+=1

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums)