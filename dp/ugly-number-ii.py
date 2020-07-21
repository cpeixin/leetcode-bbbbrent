# coding: utf-8
# Author：Brent
# Date ：2020/7/20 7:03 PM
# Tool ：PyCharm
# Describe ：

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]

if __name__ == '__main__':
    solution = Solution()
    solution.nthUglyNumber(8)