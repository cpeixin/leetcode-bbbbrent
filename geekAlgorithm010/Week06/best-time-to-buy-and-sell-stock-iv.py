# coding: utf-8
# Author：Brent
# Date ：2020/7/4 1:57 PM
# Tool ：PyCharm
# Describe ：给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2:
#
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1: return 0
        """
        正常交易的情况下，完成一次交易最少也需要两天的时间。所以有效的交易次数应该小于等于 n//2
        如果大于 n//2 ，则此种情况退化为可交易任意次的情况
        """
        if k > n // 2:
            dp_1 = [[None, None] for _ in range(n)]
            #           # 边界条件
            dp_1[0][0] = 0
            dp_1[0][1] = -prices[0]

            for i in range(1, n):
                dp_1[i][0] = max(dp_1[i - 1][0], dp_1[i - 1][1] + prices[i])
                dp_1[i][1] = max(dp_1[i - 1][1], dp_1[i - 1][0] - prices[i])
            return dp_1[-1][0]
        else:
            dp_2 = [[[None, None] for _ in range(k+1)] for _ in range(n)]
            """边界条件，分别为i=0, k=0"""
            for i in range(n):
                dp_2[i][0][0] = 0
                dp_2[i][0][1] = float('-inf')
            for k in range(k+1):
                dp_2[0][k][0] = 0
                dp_2[0][k][1] = -prices[0]

            for i in range(1, n):
                for k in range(1, k+1):
                    dp_2[i][k][0] = max(dp_2[i-1][k][0], dp_2[i-1][k][1] + prices[i])
                    dp_2[i][k][1] = max(dp_2[i-1][k][1], dp_2[i-1][k-1][0] - prices[i])

            return dp_2[-1][-1][0]

