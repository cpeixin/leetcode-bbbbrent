# coding: utf-8
# Author：Brent
# Date ：2020/6/26 3:29 PM
# Tool ：PyCharm
# Describe ：

class Solution:
    def permute(self, nums):
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

if __name__ == '__main__':
    case = Solution()
    result = case.permute([1,2,3])
    print(result)
