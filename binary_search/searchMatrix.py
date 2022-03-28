#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 10:20 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : searchMatrix.py
# @Description:编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
class Solution:
    def searchMatrix(self, matrix, target: int):
        matrix_len, matrix_high = len(matrix[0]), len(matrix)

        column_low, column_hight = 0, matrix_high - 1
        flag = False
        while column_low <= column_hight:
            column_mid = (column_hight + column_low) >> 1
            if target > matrix[column_mid][0] and target > matrix[column_mid][matrix_len-1]:
                column_low = column_mid + 1
            elif target < matrix[column_mid][0]:
                column_hight = column_mid - 1
            elif target >= matrix[column_mid][0] and target <= matrix[column_mid][matrix_len-1]:
                """再次二分查找"""
                left, right = 0, matrix_len-1
                while left <= right:
                    mid = (left+right) >> 1
                    if matrix[column_mid][mid] > target:
                        right = mid - 1
                    elif matrix[column_mid][mid] < target:
                        left = mid + 1
                    elif matrix[column_mid][mid] == target:
                        flag = True
                        break
                break
        return flag


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = solution.searchMatrix(matrix, target)
    print(result)