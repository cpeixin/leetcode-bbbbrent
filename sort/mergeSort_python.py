# coding: utf-8
# Author：Brent
# Date ：2020/9/4 4:47 PM
# Tool ：PyCharm
# Describe ：归并排序


class Solution:
    def merge_sort(self,nums):
        if len(nums) <= 1: return nums
        mid = len(nums) >> 1
        arr_left = self.merge_sort(nums[:mid])
        arr_right = self.merge_sort(nums[mid:])
        return self.merge(arr_left, arr_right)


    def merge(self, arr_left, arr_right):
        result = []
        index_left, index_right = 0, 0
        while index_left < len(arr_left) and index_right < len(arr_right):
            if arr_left[index_left] < arr_right[index_right]:
                result.append(arr_left[index_left])
                index_left+=1
            else:
                result.append(arr_right[index_right])
                index_right += 1

        if index_left == len(arr_left):
            for i in arr_right[index_right:]:
                result.append(i)
        else:
            for i in arr_left[index_left:]:
                result.append(i)

        return result

if __name__ == '__main__':
    nums = [3,2,4,5,6,7,1]
    solution = Solution()
    res = solution.merge_sort(nums)
    print(res)







