# coding: utf-8
# Author：Brent
# Date ：2020/8/17 5:59 PM
# Tool ：PyCharm
# Describe ：
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# 复杂度分析：
# 时间复杂度 O(N^2)：其中固定指针k循环复杂度 O(N)O(N)，双指针 i，j 复杂度 O(N)。
# 空间复杂度 O(1)：指针使用常数大小的额外空间。

class Solution:
    def threeSum(self, nums):
        length_nums = len(nums)
        res = []
        nums.sort()
        for index in range(length_nums-2):
            if nums[index] >= 0:
                break
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left, right = index + 1, length_nums - 1
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif sum > 0:
                    right-=1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left-1]: left += 1
        return res

