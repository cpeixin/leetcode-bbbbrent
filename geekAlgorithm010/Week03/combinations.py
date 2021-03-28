# coding: utf-8
# Author：Brent
# Date ：2020/6/26 10:26 AM
# Tool ：PyCharm
# Describe ：给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combinations

class Solution:
    def combine(self, n, k):
        result = list()
        def solve(first, k, item_list):
            if k==0: result.append(item_list)
            else:
                for i in range(first+1, n+1):
                    solve(i, k-1, item_list+[i])
        solve(0, k, [])

        return result

if __name__ == '__main__':
    case = Solution()
    result = case.combine(4, 2)
    print(result)