# coding: utf-8
# Author：Brent
# Date ：2020/10/7 8:07 AM
# Tool ：PyCharm
# Describe ：给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, index_0, index_2 = 0, 0, len(nums) - 1

        while i < index_2:
            while i < index_2 and nums[i] == 2:
                nums[i], nums[index_2] = nums[index_2], nums[i]
                index_2 -= 1

            if nums[i] == 0:
                nums[i], nums[index_0] = nums[index_0], nums[i]
                index_0 += 1
            i += 1
        return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    solution = Solution()
    res = solution.sortColors(nums)
    print(res)
