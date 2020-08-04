# coding: utf-8
# Author：Brent
# Date ：2020/8/4 10:34 PM
# Tool ：PyCharm
# Describe ：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-path-sum

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 边界条件
        if not grid: return 0
        rows = len(grid)
        columns = len(grid[0])
        # 创建dp数组
        dp = [[0] * columns for _ in range(rows)]
        # 初始化dp数组
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, columns):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]