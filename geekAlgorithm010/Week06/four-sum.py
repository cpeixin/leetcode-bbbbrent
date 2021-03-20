# coding: utf-8
# Author：Brent
# Date ：2020/7/12 3:15 PM
# Tool ：PyCharm
# Describe ：给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4: return []
        a = 0
        n = len(nums)
        nums.sort()
        res = []
        while a < n - 3:
            b = a + 1
            while b< n-2:
                c = b + 1
                d = len(nums) - 1

                while c < d:
                    # tmp = []
                    if nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]: d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                        while c < d and nums[c] == nums[c - 1]: c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                b+=1
            a+=1
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(res)
