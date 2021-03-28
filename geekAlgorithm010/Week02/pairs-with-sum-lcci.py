# coding: utf-8
# Author：Brent
# Date ：2020/6/18 1:48 PM
# Tool ：PyCharm
# Describe ：设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。
#
# 示例 1:
#
# 输入: nums = [5,6,5], target = 11
# 输出: [[5,6]]
# 示例 2:
#
# 输入: nums = [5,6,5,6], target = 11
# 输出: [[5,6],[5,6]]
# 提示：
#
# nums.length <= 100000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pairs-with-sum-lcci



def pairSums(nums, target):
    h = dict()
    res = []
    for i in range(len(nums)):
        if h.get(target - nums[i], 0) == 0:
            h[nums[i]] = h.get(nums[i], 0) + 1
        else:
            res.append([nums[i], target - nums[i]])
            h[target - nums[i]] -= 1
    return res


if __name__ == '__main__':
    nums = [5, 5, 5, 6]
    target = 11
    pairSums(nums, target)
