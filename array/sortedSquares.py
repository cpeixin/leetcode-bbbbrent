# coding: utf-8
# Author：Brent
# Date ：2020/10/16 11:21 AM
# Tool ：PyCharm
# Describe ：给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。


class Solution:
    def sortedSquares(self, A):
        n = len(A)
        ans = [0] * n

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                ans[pos] = A[i] * A[i]
                i += 1
            else:
                ans[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        return ans


if __name__ == '__main__':
    A = [-4,-1,0,3,10]
    res = Solution().sortedSquares(A)
