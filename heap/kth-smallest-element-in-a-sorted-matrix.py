# coding: utf-8
# Author：Brent
# Date ：2020/6/18 8:42 AM
# Tool ：PyCharm
# Describe ：给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
#
#  
#
# 示例：
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
import heapq
# from heap.heapq_showtree import show_tree


def kthSmallest(matrix, k):
    if not matrix or not matrix[0]:
        return -1
    heap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            nextVal = -matrix[row][col]
            if len(heap) < k:
                heapq.heappush(heap, nextVal)
            elif nextVal > heap[0]:
                heapq.heappushpop(heap, nextVal)
            # show_tree(heap)
    return -heap[0]


def kthSmallest_1(matrix, k):
    n = len(matrix)

    def check(mid):
        i, j = n - 1, 0
        num = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                num += i + 1
                j += 1
            else:
                i -= 1
        return num >= k

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    kthSmallest_1(matrix, 5)
