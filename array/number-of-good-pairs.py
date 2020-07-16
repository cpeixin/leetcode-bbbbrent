# coding: utf-8
# Author：Brent
# Date ：2020/7/12 10:36 AM
# Tool ：PyCharm
# Describe ：给你一个整数数组 nums 。
#
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
#
# 返回好数对的数目。
#
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1: return []
        left = 0
        pairs = 0

        while left <= len(nums) - 2:
            for right in range(left + 1, len(nums)):
                if nums[left] == nums[right]: pairs+=1
            left+=1
        return pairs

if __name__ == '__main__':
    solution = Solution()
    print(solution.numIdenticalPairs([1,1,1,1]))