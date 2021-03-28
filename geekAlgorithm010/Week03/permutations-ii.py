# coding: utf-8
# Author：Brent
# Date ：2020/6/26 5:47 PM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return[]
        nums.sort()
        n = len(nums)
        res = []

        def helper2(nums, temp_list, length):
                if length == n and temp_list not in res:
                    res.append(temp_list)
                for i in range(len(nums)):
                    helper2(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)
        helper2(nums, [], 0)
        return res

if __name__ == '__main__':
    case = Solution()
    result = case.permuteUnique([1,2,1])
    print(result)