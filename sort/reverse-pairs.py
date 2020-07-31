# coding: utf-8
# Author：Brent
# Date ：2020/7/31 2:49 PM
# Tool ：PyCharm
# Describe ：给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
# 输入: [1,3,2,3,1]
# 输出: 2
# 示例 2:
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-pairs
class Solution(object):
    def __init__(self):
        self.cnt = 0
    def reversePairs(self, nums):
        def msort(lst):
            # merge sort body
            L = len(lst)
            if L <= 1:                          # base case
                return lst
            left = msort(lst[:int(L/2)])
            right =  msort(lst[int(L/2):])   # recursive case
            return merger(left, right)
        def merger(left, right):
            # merger
            l, r = 0, 0                         # increase l and r iteratively
            while l < len(left) and r < len(right):
                if left[l] <= 2*right[r]:
                    l += 1
                else:
                    self.cnt += len(left)-l     # add here
                    r += 1
            return sorted(left+right)           # I can't avoid TLE without timsort...

        msort(nums)
        return self.cnt

if __name__ == '__main__':
    array = [2,4,3,5,1]
    solution = Solution()
    cnt = solution.reversePairs(array)
    print(cnt)