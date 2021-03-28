# coding: utf-8
# Author：Brent
# Date ：2020/7/19 10:46 AM
# Tool ：PyCharm
# Describe ：斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 给定 N，计算 F(N)。
#
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fibonacci-number


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        : dp数组
        """

        if N<=1: return N
        dp = [0] * N
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    solution.fib(5)