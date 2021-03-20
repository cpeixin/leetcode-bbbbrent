# coding: utf-8
# Author：Brent
# Date ：2020/7/15 9:48 PM
# Tool ：PyCharm
# Describe ：一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 定义dp二维数组
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # 起点为dp[0][0],所以没有m+1, n+1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths_1(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    def uniquePaths_2(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]



if __name__ == '__main__':
    # solution = Solution()
    # solution.uniquePaths_2(4,4)
    m, n = 4,4
    dp = [[1] * n, [[1] + [0] * (n - 1) for _ in range(m - 1)]]
    print(dp)