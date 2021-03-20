# coding: utf-8
# Author：Brent
# Date ：2020/7/20 12:53 AM
# Tool ：PyCharm
# Describe ：在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-square

class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix: return 0
        rows, columns = len(matrix), len(matrix[0])
        # 创建dp数组
        dp = [[0] * columns for _ in range(rows)]
        maxSide = 0

        for i in range(rows):
            for j in range(columns):
                # 矩阵中只有两种值 0 ， 1
                if matrix[i][j] == '1':
                    #两种情况，边界和内部
                    if i == 0 or j == 0: dp[i][j] = 1
                    else:
                        # 取左块，上块，左上块
                        dp[i][j] = min(dp[i][j],dp[i][j],dp[i][j])+1
                    maxSide = max(maxSide,dp[i][j])
        return maxSide * maxSide