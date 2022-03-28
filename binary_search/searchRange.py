#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 7:40 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : searchRange.py
# @Description:

class Solution:
    def searchRange(self, nums, target):
        """特例判断"""
        res = [-1, -1]
        if not nums: return res

        left, right = 0, len(nums) - 1

        res = [-1, -1]

        while left <= right:
            mid = (right + left) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = [mid, mid]
                # if mid > 0:
                flag_l, flag_r = mid - 1, mid + 1
                # else:
                #     return res
                while flag_l >= 0 and nums[flag_l] == target:
                    res[0] = flag_l
                    flag_l -= 1
                while flag_r < len(nums) and nums[flag_r] == target:
                    res[1] = flag_r
                    flag_r += 1
                break
        return res


if __name__ == '__main__':
    solution = Solution()
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    nums = [1]
    target = 1
    result = solution.searchRange(nums, target)
    print(result)
