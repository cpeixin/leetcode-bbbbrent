# coding: utf-8
# Author：Brent
# Date ：2020/7/5 9:26 PM
# Tool ：PyCharm
# Describe ：实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid == x: return mid
            elif mid*mid > x: right = mid - 1
            else: left = mid +1
        return right

if __name__ == '__main__':
    solution = Solution()

    result = solution.mySqrt(4)
    print(result)
