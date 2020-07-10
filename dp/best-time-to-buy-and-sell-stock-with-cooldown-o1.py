# coding: utf-8
# Author：Brent
# Date ：2020/7/10  10:20 PM
# Tool ：PyCharm
# Describe ：给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0

        # 使用交换变量的方式来代替状态方程，可以降低空间复杂度
        profit_i_0 = 0
        profit_i_1 = float('-inf')
        profit_pre = 0

        for price in prices:
            tmp_profit = profit_i_0
            profit_i_0 = max(profit_i_0, profit_i_1 + price)
            profit_i_1 = max(profit_i_1, profit_pre - price)
            profit_pre = tmp_profit
        return profit_i_0
