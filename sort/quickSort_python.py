# coding: utf-8
# Author：Brent
# Date ：2020/9/4 4:10 PM
# Tool ：PyCharm
# Describe ：快速排序
import random


class Solution:

    def quick(self, nums):
        left_index = 0
        right_index = len(nums)-1
        res = self.quickSort(nums,left_index,right_index)
        return res


    def quickSort(self, nums, left_index, right_index):
        if left_index > right_index: return
        pivot = self.partition(nums, left_index, right_index)
        self.quickSort(nums, left_index, pivot-1)
        self.quickSort(nums, pivot+1, right_index)
        return nums


    def partition(self, nums, left_index, right_index):
        pivot = nums[left_index]
        mark = left_index#为比pivot小数值计数
        for i in range(left_index+1, right_index+1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[left_index], nums[mark] = nums[mark], nums[left_index]
        return mark

    def partition_random(self, nums, left_index, right_index):
        # 加入随机化
        random_num = random.randint(left_index, right_index)
        nums[random_num], nums[left_index] = nums[left_index], nums[random_num]

        pivot = nums[left_index]
        mark = left_index#为比pivot小数值计数
        for i in range(left_index+1, right_index+1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[left_index], nums[mark] = nums[mark], nums[left_index]
        return mark


if __name__ == '__main__':
    nums = [3,2,4,5,6,7,1]
    solution = Solution()
    res = solution.quick(nums)
    print(res)



