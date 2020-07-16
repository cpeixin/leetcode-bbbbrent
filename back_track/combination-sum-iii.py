# coding: utf-8
# Author：Brent
# Date ：2020/7/13 9:20 AM
# Tool ：PyCharm
# Describe ：找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def combinationSum3(self, k, n):
        if k == 0: return []
        nums = [1,2,3,4,5,6,7,8,9]
        res = []
        def backtrack(nums, n, tmp):
            if n == 0 and len(tmp) == k: res.append(tmp)
            if n < 0: return
            for i in range(len(nums)):
                backtrack(nums[i+1:], n - nums[i], tmp + [nums[i]])
        backtrack(nums, n, [])
        return res

