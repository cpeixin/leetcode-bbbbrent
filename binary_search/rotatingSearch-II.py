#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 10:04 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : rotatingSearch.py
# @Description:整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


if __name__ == '__main__':
    solution = Solution()
    array = [1, 0, 1, 1, 1]
    target = 0
    result = solution.search(array, target)
    print(result)
