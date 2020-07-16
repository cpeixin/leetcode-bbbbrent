# coding: utf-8
# Author：Brent
# Date ：2020/7/13 12:33 AM
# Tool ：PyCharm
# Describe ：给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates: return []
        if min(candidates) > target: return []
        candidates.sort()
        res = []
        # 路径，选择列表
        def backtrack(candidates, target, tmp):
            # 满足结束条件
            if target == 0 and tmp not in res: res.append(tmp)
            if target < 0: return
            for i in range(len(candidates)):
                # 做选择
                if candidates[i] > target: break
                # 选择列表  路径。 因为不能重复选择，所以candidates[i+1:]
                backtrack(candidates[i+1:], target - candidates[i], tmp + [candidates[i]])
        backtrack(candidates, target, [])
        return res