#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 6:12 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : threeSum.py
# @Description:给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#  
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
#
# 输入：nums = []
# 输出：[]
# 示例 3：
#
# 输入：nums = [0]
# 输出：[]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 3: return res

        nums = sorted(nums)

        left, mid, right = 0, 1, len(nums) - 1
        while left < mid and mid < right:
            while mid < right:
                if nums[left] + nums[mid] + nums[right] == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while nums[mid] == nums[mid+1] and mid < right:
                        mid += 1
                    while nums[right] == nums[right - 1] and mid < right:
                        right -= 1
                elif nums[left] + nums[mid] + nums[right] > 0:
                    right -= 1
                    while nums[right] == nums[right - 1] and mid < right:
                        right -= 1
                else:
                    mid += 1
                    while nums[mid] == nums[mid+1] and mid < right:
                        mid += 1
            left += 1
            mid = left + 1
            right = len(nums) - 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)
