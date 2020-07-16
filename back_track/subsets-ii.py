# coding: utf-8
# Author：Brent
# Date ：2020/7/11 9:28 PM
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
        # 结果集
        res = []
        n = len(nums)
        """
        因为给定数组包含重复元素，需要先对nums排序，
        排序后nums里相同的元素必定相邻
        然后在遍历解空间树的时候，要做一个去重的操作，
        当遇到重复出现，也就是和前面相邻元素相同的时候，
        直接跳过该节点，不让它向下递归
        """
        nums.sort()
        def backtrack(index, tmp):
            if tmp not in res: res.append(tmp)
            for i in range(index, n):
                backtrack(i+1, tmp+[nums[i]])
        backtrack(0, [])
        return res

    def subsetsWithDup_1(self, nums):
        if not nums: return []
        nums.sort()
        res = []
        def backtrack(nums, tmp):
            if tmp not in res: res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[i+1:], tmp+[nums[i]])
        backtrack(nums, [])
        return res


if __name__ == '__main__':
    case = Solution()
    result = case.subsetsWithDup([1, 2, 2])
    print(result)
