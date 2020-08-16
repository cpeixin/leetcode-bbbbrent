# coding: utf-8
# Author：Brent
# Date ：2020/8/11 10:30 AM
# Tool ：PyCharm
# Describe ：输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof

from typing import List


# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         def partition(low, high):
#             counter = low
#             pivot = arr[high]
#             for j in range(low+1, high+1):
#                 if arr[j] <= pivot:
#                     arr[counter], arr[j] = arr[j], arr[counter]
#                     counter += 1
#             arr[counter+1], arr[high] = arr[high], arr[counter+1]
#             return counter+1
#
#         def quickSort(low, high):
#             if low<high:
#                 pivot = partition(low, high)
#                 if pivot==k: return
#                 if pivot>k-1: quickSort(low, pivot-1)
#                 if pivot<k-1: quickSort(pivot+1, high)
#         quickSort(0, len(arr)-1)
#         return arr[:k]

# class Solution:
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         def partition(start, end):
#             pivot = arr[end]
#             counter = start - 1
#             for i in range(start+1, end+1):
#                 if arr[i] <= pivot:
#                     # i, counter相等，则原地不变
#                     # i, counter不相等，则左右调换，大值向后移
#                     counter += 1
#                     arr[counter], arr[i] = arr[i], arr[counter]
#
#             arr[end], arr[counter+1] = arr[counter+1], arr[end]
#             return counter+1
#
#         def quickSort(start, end):
#             if start < end:
#                 pivot = partition(start, end)
#                 if pivot == k: return
#                 if pivot > k-1: quickSort(start, pivot-1)
#                 if pivot < k-1: quickSort(pivot+1, end)
#         quickSort(0, len(arr)-1)
#         return arr[:k]

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 方法一:partition方法(基于快速排序)
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            print(index)
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low


if __name__ == '__main__':
    arr = [3, 9, 2, 4, 7, 5, 6]
    k = 3
    solution = Solution()
    res = solution.getLeastNumbers(arr, k)
    print(res)