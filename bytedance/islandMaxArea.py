# coding: utf-8
# Author：Brent
# Date ：2020/8/17 10:50 PM
# Tool ：PyCharm
# Describe ：给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
#
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#
#
#
# 示例 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
#
# 示例 2:
#
# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。

class Solution:
    def island_max_area(self, grid):
        if not grid: return 0
        rows = len(grid)
        columns = len(grid[0])
        maxArea = 0

        visited = [[False] * columns for _ in range(rows)]

        def dfs(i, j, visited):
            visited[i][j] = True
            res = 1
            for _i, _j in ((1, 0),(-1, 0),(0, 1),(0, -1)):
                new_i, new_j = i+_i, j+_j
                if 0 <= new_i < rows and 0 <= new_j < columns and not visited[new_i][new_j] and grid[new_i][new_j] == 1:
                    res+=dfs(new_i, new_j, visited)
            return res


        for i in range(rows):
            for j in range(columns):
                if not visited[i][j] and grid[i][j] == 1:
                    maxArea = max(dfs(i, j, visited), maxArea)
        return maxArea

if __name__ == '__main__':
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    res = solution.island_max_area(grid)
    print(res)