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
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        # 特判
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        # 从第 1 行、第 1 格开始，对每一格尝试进行一次 DFS 操作
        for i in range(m):
            for j in range(n):
                # 只要是陆地，且没有被访问过的，就可以使用 DFS 发现与之相连的陆地，并进行标记
                if not marked[i][j] and grid[i][j] == '1':
                    # count 可以理解为连通分量，你可以在深度优先遍历完成以后，再计数，
                    # 即这行代码放在【位置 1】也是可以的
                    count += 1
                    self.__dfs(grid, i, j, m, n, marked)
                    # 【位置 1】
        return count

    def __dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.__dfs(grid, new_i, new_j, m, n, marked)



    def numIslands_dfs(self, grid: [[str]]) -> int:

        def dfs(grid, i, j, rows, columns):
            # 终止条件：
            # (i, j) 越过矩阵边界;
            # grid[i][j] == 0，代表此分支已越过岛屿边界。
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
                    count += 1
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




