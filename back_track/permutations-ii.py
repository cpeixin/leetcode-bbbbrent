# coding: utf-8
# Author：Brent
# Date ：2020/6/26 5:47 PM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def permuteUnique(self, nums):
        if not nums: return[]
        nums.sort()
        res = []
        def backtrack(nums, temp_list):
                if not nums and temp_list not in res:
                    res.append(temp_list)
                for i in range(len(nums)):
                    backtrack(nums[:i] + nums[i + 1:], temp_list + [nums[i]])
                backtrack(nums, [])
        return res

if __name__ == '__main__':
    case = Solution()
    result = case.permuteUnique([1,2,1])
    print(result)