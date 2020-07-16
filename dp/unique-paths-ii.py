# coding: utf-8
# Author：Brent
# Date ：2020/7/16 10:37 PM
# Tool ：PyCharm
# Describe ：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths-ii

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                # 有障碍物
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    # 处理边界问题
                    if i == j == 0:
                        obstacleGrid[i][j] = 1
                    else:
                        # 如果 i  为 0，则是第0行，无法获取上层数值，所以只能为同层左边元素的值
                        up = obstacleGrid[i - 1][j] if i != 0 else 0
                        # 如果 j 为 0， 则是第0列，无法获取同层左元素，所以只能为同列上层元素的值
                        left = obstacleGrid[i][j - 1] if j != 0 else 0
                        obstacleGrid[i][j] = up + left
        return obstacleGrid[-1][-1]

    def uniquePathsWithObstacles_1(self, obstacleGrid):
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            if obstacleGrid[0][0]:
                return 0

            dp = [0] * (n + 1)
            dp[1] = 1
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if obstacleGrid[i - 1][j - 1] == 0:
                        dp[j] += dp[j - 1]
                    else:
                        dp[j] = 0
            return dp[-1]


if __name__ == '__main__':
    a = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    solution = Solution()
    solution.uniquePathsWithObstacles_1(a)
