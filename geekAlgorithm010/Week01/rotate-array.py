# coding: utf-8
# Author：Brent
# Date ：2020/6/13 3:29 PM
# Tool ：PyCharm
# Describe ：给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]


class Solution(object):
    def rotate(self, nums, k):
        #反转前k个位置元素
        k = k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
