# coding: utf-8
# Author：Brent
# Date ：2020/7/3 07:20 AM
# Tool ：PyCharm
# Describe ：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
#
#  
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 价格数组长度
        n = len(prices)

        """
        base case:
        dp[-1][k][0] = dp[i][0][0] = 0
        dp[-1][k][1] = dp[i][0][1] = float('-inf')
        是经过分析题的过程中，总结出来的
        下面两个变量的命名，profit_i_(0 or 1), i代表的是天数，0，1后缀代表的是，当前时候持有股票，0：没有持有，1：持有
        定义下面两个变量则可以表示当前的两种状态， 要么持有股票，要么没有持有股票
        dp[i][0] = 0;
        解释：
        dp[i][0] = max(dp[-1][0], dp[-1][1] + prices[i])
                 = max(0, -infinity + prices[i]) = 0
        dp[i][1] = -prices[i]
        解释：
        dp[i][1] = max(dp[-1][1], dp[-1][0] - prices[i])
                 = max(-infinity, 0 - prices[i]) 
                 = -prices[i]
        """
        profit_i_0 = 0
        profit_i_1 = float('-inf')
        # 遍历每一天
        for i in range(n):
            """
            状态转移方程：
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            下面两行核心计算步骤就是上面的状态方程转换过来的。这里注意 k-1 ，我们这里将 买入操作 进行减1，也就是减少一次交易次数，dp[i-1][k-1][0]为0，则省去
            """
            profit_i_0 = max(profit_i_0, profit_i_1+prices[i])# max(选择rest,选择sell)
            profit_i_1 = max(profit_i_1, -prices[i])# max(选择rest,选择buy)
        return profit_i_0


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    profit = solution.maxProfit(prices)
    print(profit)
