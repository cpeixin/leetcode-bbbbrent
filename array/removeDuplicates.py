#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 3:45 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : removeDuplicates.py
# @Description:
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return nums
        slow = 0
        count = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    res = solution.removeDuplicates(nums)
    print(res)
