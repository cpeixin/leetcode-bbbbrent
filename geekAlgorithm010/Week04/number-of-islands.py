# coding: utf-8
# Author：Brent
# Date ：2020/7/1 4:21 PM
# Tool ：PyCharm
# Describe ：给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#  
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
from collections import deque
from typing import List


class Solution:

    def numIslands_dfs(self, grid: [[str]]) -> int:
        def dfs(grid, i, j, rows, columns):
            if not 0 <= i < rows or 0 <= j < columns or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(grid, i + 1, j, rows, columns)
            dfs(grid, i - 1, j, rows, columns)
            dfs(grid, i, j + 1, rows, columns)
            dfs(grid, i, j - 1, rows, columns)

        count = 0
        rows = len(grid)
        if rows == 0: return 0
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    dfs(grid, i, j, rows, columns)
        return count

    def numIslands_bfs(self, grid: [[str]]) -> int:
        def bfs(grid, i, j):
            queue = [[i, j]]
            while queue:
                [i, j] = queue.pop(0)
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count


if __name__ == '__main__':
    # grid = [['1', '1', '1', '1', '0'],
    #         ['1', '1', '0', '1', '0'],
    #         ['1', '1', '0', '0', '0'],
    #         ['0', '0', '0', '0', '0']]
    grid = []
    solution = Solution()
    result = solution.numIslands_dfs(grid)
    print(result)
