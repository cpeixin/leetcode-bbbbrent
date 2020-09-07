# coding: utf-8
# Author：Brent
# Date ：2020/9/7 4:15 PM
# Tool ：PyCharm
# Describe ：


from typing import List


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero = 0
        two = size

        i = 0

        while i < two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(nums, i, two)
        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = [2,0,2,1,1,0]
    res = solution.sortColors(nums)
    print(res)