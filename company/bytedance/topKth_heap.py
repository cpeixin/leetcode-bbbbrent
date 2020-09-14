# coding: utf-8
# Author：Brent
# Date ：2020/8/18 5:53 PM
# Tool ：PyCharm
# Describe ：
import heapq


from typing import List
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums or k == 0: return None
        heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:
                    heapq.heapreplace(heap, nums[i])
        return heap[0]

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

    k = 4
    solution.findKthLargest(nums, k)