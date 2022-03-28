#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 5:14 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : removeDuplicatesII.py
# @Description:
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    solution = Solution()
    res = solution.removeDuplicates(nums)
    print(res)
