# coding: utf-8
# Author：Brent
# Date ：2020/8/20 8:15 PM
# Tool ：PyCharm
# Describe ：给定一个未排序的整数数组，找出最长连续序列的长度。
#
# 要求算法的时间复杂度为 O(n)。
#
# 示例:
#
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。


class solution:
    def longestConsecutive(self, nums):
        longest = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                curr_num = num
                curr_longth = 1

                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_longth += 1

                longest = max(longest, curr_longth)

        return longest


if __name__ == '__main__':
    nums = [4, 100, 200, 1, 3, 2, 4]
    solution = solution()
    print(solution.longestConsecutive(nums))