# coding: utf-8
# Author：Brent
# Date ：2020/8/3 11:01 PM
# Tool ：PyCharm
# Describe ：



n=3
m=7
dp = [[1] * m for _ in range(n)]
dp1 = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
dp2 = [[0 for col in range(m)] for row in range(n)]
print(dp)
print(dp1)
print(dp2)