#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/12 11:03 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : findDiagonalOrder.py
# @Description:
#
# class Solution:
#     def findDiagonalOrder(self, matrix):
#         rows = len(matrix)
#         columns = len(matrix[0])
#         roll_num = rows + columns - 1
#         res_array = []
#         index_x = 0
#         index_y = 0
#
#         for i in range(roll_num):
#             if i%2==0:
#                 res_array.append(matrix[x,y])
#             else:
import collections


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix: return []
        lookup = collections.defaultdict(list)
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                lookup[j + i].append(matrix[i][j])
        res = []
        flag = True
        for k, v in sorted(lookup.items()):
            if flag:
                res.extend(v[::-1])
            else:
                res.extend(v)
            flag = not flag
        return res
if __name__ == '__main__':
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    res = Solution().findDiagonalOrder(matrix)
    print(res)