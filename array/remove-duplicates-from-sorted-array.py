# coding: utf-8
# Team : Quality Management Center
# Author：Brent
# Date ：2020/6/13 3:01 PM
# Tool ：PyCharm
# Describe ： 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        slow_index = 0
        for fast_index in range(1, len(nums)):
            if nums[fast_index] != nums[slow_index]:
                slow_index+=1
                nums[slow_index] = nums[fast_index]
        return slow_index+1
