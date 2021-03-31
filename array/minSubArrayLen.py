#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 8:22 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : minSubArrayLen.py
# @Description:给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/array-and-string/c0w4r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans



if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    res = solution.minSubArrayLen(target, nums)
    print(res)
