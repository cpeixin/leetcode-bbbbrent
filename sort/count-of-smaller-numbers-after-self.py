# coding: utf-8
# Author：Brent
# Date ：2020/9/2 11:38 PM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return 0
        res = []
        for i in range(len(nums)):
            tmp = self.partition(0, len(nums) - i - 1, nums[i:len(nums)])
            res.append(tmp)
        return res

    def partition(self, left, right, nums):
        pivot = nums[left]
        mark = 0
        while left <= right:
            if pivot > nums[left]:
                mark += 1
            left += 1
        return mark


if __name__ == '__main__':
    solution = Solution()
    nums = [5,2,6,1]
    res = solution.countSmaller(nums)
    print(res)