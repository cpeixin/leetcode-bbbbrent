# coding: utf-8
# Author：Brent
# Date ：2020/10/28 10:21 PM
# Tool ：PyCharm
# Describe ：给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
#
import collections
from _ast import List


class Solution:
    def uniqueOccurrences(self, arr):
        nums = []
        count_dict = collections.defaultdict(int)
        for i in arr:
            count_dict[i] += 1

        for num in count_dict.keys():
            if count_dict[num] in nums:
                return False
            nums.append(count_dict[num])
        return True

if __name__ == '__main__':
    arr = [1,2,2,1,1,3]

    res = Solution().uniqueOccurrences(arr)

    print(res)