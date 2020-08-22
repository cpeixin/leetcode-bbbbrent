# coding: utf-8
# Author：Brent
# Date ：2020/8/21 10:52 PM
# Tool ：PyCharm
# Describe ：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
#
#输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1: return 0

        dp = [[None,None] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[-1][-1]

    def maxProfit_1(self, prices):
        if not prices or len(prices) == 1: return 0

        profit_0 = 0
        profit_1 = -prices[0]

        for i in range(1, len(prices)):
            profit_0 = max(profit_0, profit_1 + prices[i])
            profit_1 = max(profit_1, - prices[i])
        return profit_0