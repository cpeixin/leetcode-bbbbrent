# coding: utf-8
# Author：Brent
# Date ：2020/6/27 9:28 AM
# Tool ：PyCharm
# Describe ：给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets-ii
class Solution(object):
    def subsetsWithDup(self, nums):
        if not nums: return []
        n = len(nums)
        nums.sort()
        res = []
        def backtrack(first, temp_list):
            if temp_list not in res: res.append(temp_list)
            for i in range(first, n):
                backtrack(i+1, temp_list+[nums[i]])
        backtrack(0, [])
        return res


if __name__ == '__main__':
    case = Solution()
    result = case.subsetsWithDup([1, 2, 2])
    print(result)
