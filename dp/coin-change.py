# coding: utf-8
# Author：Brent
# Date ：2020/7/14 11:35 PM
# Tool ：PyCharm
# Describe ：给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#  
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change


class Solution:
    def coinChange_up_2_down(self, coins, amount):
        # 定义备忘录
        cache = {}

        """递归函数，选择状态，原问题和子问题 变化的变量"""
        def dp(tmp_amount):
            # 避免重复计算
            if tmp_amount in cache: return cache[tmp_amount]
#           base case
            if tmp_amount == 0: return 0
            if tmp_amount < 0: return -1
            # 初始化结果
            res = float('inf')
            for coin in coins:
                sub_problem = dp(tmp_amount - coin)
                # 判断前一个子问题是否满足
                if sub_problem == -1: continue
                res = min(res, sub_problem + 1)
            # 子问题结果加入备忘录
            cache[tmp_amount] = res if res != float('inf') else -1
            return cache[tmp_amount]
        return dp(amount)



    def coinChange_down_2_up(self, coins, amount):
        """初始化dp 数组
        amount + 1, 预留 0 的位置
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange_down_2_up([1,2,5], 11))