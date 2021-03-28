# coding: utf-8
# Author：Brent
# Date ：2020/6/27 8:47 AM
# Tool ：PyCharm
# Describe ：给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        res = []
        n = len(nums)
        def backtrack(first, temp_list):
            res.append(temp_list)
            for i in range(first, n):
                backtrack(i+1, temp_list+[nums[i]])
        backtrack(0, [])
        return res




if __name__ == '__main__':
    case = Solution()
    result = case.subsets([1, 2, 3])
    print(result)
