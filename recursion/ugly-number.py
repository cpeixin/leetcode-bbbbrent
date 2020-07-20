# coding: utf-8
# Author：Brent
# Date ：2020/7/20 4:07 PM
# Tool ：PyCharm
# Describe ：编写一个程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        if num == 1: return True
        if num % 2 == 0: return self.isUgly(num // 2)
        if num % 3 == 0: return self.isUgly(num // 3)
        if num % 5 == 0: return self.isUgly(num // 5)
        return False

if __name__ == '__main__':
    solution = Solution()
    solution.isUgly(12)