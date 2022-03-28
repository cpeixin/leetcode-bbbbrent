#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 9:57 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : majorityElement.py
# @Description:
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                majority = nums[i]
            count += (1 if nums[i] == majority else -1)
        return majority


if __name__ == '__main__':
    nums = [3,2,3]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)
