#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 2:23 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : majorityElement-qs.py
# @Description:
import random


class Solution(object):
    def majorityElement(self, nums):
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = (left + right) >> 1
        return self.quickSort(nums, left, right, mid)

    def quickSort(self, nums, left, right, mid):
        if left > right: return
        pivot = self.partition(nums, left, right)
        if pivot == mid:
            return nums[mid]
        if pivot > mid:
            return self.quickSort(nums, left, pivot - 1, mid)
        else:
            return self.quickSort(nums, pivot + 1, right, mid)

    def partition(self, nums, left_index, right_index):
        randoms = random.randint(left_index, right_index)
        nums[left_index], nums[randoms] = nums[randoms], nums[left_index]

        pivot = nums[left_index]
        mark = left_index
        for i in range(left_index + 1, right_index + 1):
            if nums[i] < pivot:
                mark += 1
                nums[i], nums[mark] = nums[mark], nums[i]
        nums[left_index], nums[mark] = nums[mark], nums[left_index]
        return mark


if __name__ == '__main__':
    nums = [3,3,4]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)
