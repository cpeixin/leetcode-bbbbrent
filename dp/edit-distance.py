# coding: utf-8
# Author：Brent
# Date ：2020/7/20 11:31 PM
# Tool ：PyCharm
# Describe ：给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        # 定义dp数组
        dp = [[0] * (n+1) for i in range(m+1)]
        # 初始化dp 边界条件, 当""子串要进行转换的最小步骤
        for i in range(1, n+1):
            dp[0][i] = i
        for j in range(1, m+1):
            dp[j][0] = j

        # 自底向上开始遍历
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
        return dp[-1][-1]




if __name__ == '__main__':
    solution = Solution()
    solution.minDistance("scdfadsfa", "asc")

