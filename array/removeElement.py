#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 8:50 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : removeElement.py
# @Description:给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 示例 1：
#
# 输入：nums = [3,2,2,3], val = 3 输出：2, nums = [2,2] 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为
# 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。


class Solution:
    def removeElement(self, nums, val):
        if not nums: return nums
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

    def removeElementII(self, nums, val):
        if len(nums) == 0: return 0
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right-=1
            else:
                left +=1
        return left


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution = Solution()
    res = solution.removeElementII(nums, val)
    print(res)
