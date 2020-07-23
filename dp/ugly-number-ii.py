# coding: utf-8
# Author：Brent
# Date ：2020/7/20 7:03 PM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        : 动态方程来做
        """
        if n <= 1: return n
        # 创建dp数组
        dp = [0] * n
        # 初始化dp数组
        dp[0] = 1
        num_2, num_3, num_5 = 0, 0, 0
        for i in range(1, n):
            # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
            dp[i] = min(2*dp[num_2], 3*dp[num_3], 5*dp[num_5])
            if dp[i] >= 2*dp[num_2]: num_2 += 1
            if dp[i] >= 3*dp[num_3]: num_3 += 1
            if dp[i] >= 5*dp[num_5]: num_5 += 1
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    solution.nthUglyNumber(8)