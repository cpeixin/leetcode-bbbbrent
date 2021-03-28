# coding: utf-8
# Author：Brent
# Date ：2020/6/13 5:05 PM
# Tool ：PyCharm
# Describe ：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#  
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 链接：https://leetcode-cn.com/problems/two-sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 借助Map,python中为dict
        dict = {}
        for index in range(len(nums)):
            if not nums[index] in dict:
                # 在map中存储能和nums[index]相加为target的值
                dict[target-nums[index]] = index
            else:
                return [dict[nums[index]], index]
