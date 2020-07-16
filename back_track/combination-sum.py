# coding: utf-8
# Author：Brent
# Date ：2020/7/12 10:17 PM
# Tool ：PyCharm
# Describe ：给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum

class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates: return []
        # 题目规定，都是正整数
        if min(candidates) > target: return []
        candidates.sort()
        res = []

        def backtrack(candidates, target, tmp):
            if target == 0: res.append(tmp)
            # 这一步可以理解为剪枝么？
            if target < 0: return
            for i in range(len(candidates)):
                # 做选择
                if candidates[i] > target: break
                # 可重复选择
                backtrack(candidates[i:], target - candidates[i], tmp + [candidates[i]])
        backtrack(candidates, target, [])
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2,3,6,7], 7))
