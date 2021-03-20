# coding: utf-8
# Author：Brent
# Date ：2020/8/5 10:31 PM
# Tool ：PyCharm
# Describe ：数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  示例 2:
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
# 注意：
#
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。


class Solution(object):
    def minCostClimbingStairs(self, cost):
        # 防止越界，设置楼顶为0花费
        cost.append(0)
        # 定义状态数组
        dp = [0] * len(cost)
        # 初始化
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            # 和爬楼梯相似，i级台阶是从 i-1一步上来的  或者  i-2 两步上来的。
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        return dp[-1]

    def minCostClimbingStairs_1(self, cost):
        # 防止越界，设置楼顶为0花费
        cost.append(0)
        a = cost[0]
        b = cost[1]

        for i in range(2, len(cost)):
            c = min(b + cost[i], a + cost[i])
            a, b = b, c
        return c



if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    solution = Solution()
    print(solution.minCostClimbingStairs_1(cost))
