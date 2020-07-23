# coding: utf-8
# Author：Brent
# Date ：2020/7/6 10:38 PM
# Tool ：PyCharm
# Describe ：给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            res.append([1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i - 1)] + [1])
        return res[rowIndex][:]


# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
#         else:
#             res = [[1], [1, 1]]
#         for i in range(2, rowIndex + 1):
#             res.append([1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i - 1)] + [1])
#         return res[rowIndex][:]

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         res = [1]
#         for i in range(rowIndex):
#             res += [1]
#             for j in range(i, 0, -1):
#                 res[j] = res[j] + res[j-1]
#         return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(5))