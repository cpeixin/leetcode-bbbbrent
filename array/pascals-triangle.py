# coding: utf-8
# Author：Brent
# Date ：2020/7/29 10:36 PM
# Tool ：PyCharm
# Describe ：给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        res = self.generate(numRows-1)
        res.append([1]+[res[-1][i-1]+res[-1][i] for i in range(1, numRows-1)]+[1])
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))