# coding: utf-8
# Author：Brent
# Date ：2020/9/7 1:46 PM
# Tool ：PyCharm
# Describe ：给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#  
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
import collections
import random


class Solution:
    def topKFrequent(self, nums, k):
        if not nums: return []
        count_dict = collections.defaultdict(int)

        for i in nums:
            count_dict[i] += 1

        array = []

        for key in count_dict.keys():
            array.append((count_dict[key], key))

        left, right = 0, len(array)-1


        index = self.partition(array, k)


        if index > k-1:
            self.partition(array[:index], k)
        elif index < k-1:
            self.partition(array[index+1:], k)

        return [array[i][1] for i in range(index)]



    def partition(self, nums, k):
        left = 0
        right = len(nums) - 1
        tmp_index = random.randint(left, right)
        nums[left], nums[tmp_index] = nums[tmp_index], nums[left]
        pivot = nums[left]
        mark = left

        for i in range(left + 1, right + 1):
            if nums[i][0] > pivot[0]:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[mark], nums[left] = nums[left], nums[mark]
        return mark






if __name__ == '__main__':
    nums = [1, 1, 1, 1, 4, 4, 5, 3, 2, 6, 6, 6, 7, 8, 8, 9]
    k = 2
    solution = Solution()
    print(solution.topKFrequent(nums, k))
