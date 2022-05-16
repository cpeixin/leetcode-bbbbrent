#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 6:51 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : merge.py
# @Description:
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，
# 分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，
# 应忽略。nums2 的长度为 n

# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

# 常规解题思路 ：其实这道题就是归并排序 partition 的过程（将两个有序的数列合并成一个有序数列），直观的思路是新建一个新的数列，
# 遍历 nums1 和 nums2 这两个数列，将新建的数列有序后又赋值给 nums1后返回。其实还有一种方法不需要开辟新的空间。
#
# 尾插法
# 由于 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素，所以从 k=m+n-1 开始，分别遍历 nums1[m...0] 和 nums2[n...0] 中选取值大的。


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1_index = m - 1
        # nums2_index = n - 1
        # while nums1_index >= 0 and nums2_index >= 0:
        #     if nums1[nums1_index] >= nums2[nums2_index]:
        #         nums1[nums1_index + nums2_index + 1] = nums1[nums1_index]
        #         nums1_index -= 1
        #     else:
        #         nums1[nums1_index + nums2_index + 1] = nums2[nums2_index]
        #         nums2_index -= 1
        # return nums1

        m_index, n_index, num1_index = m - 1, n - 1, m + n - 1
        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] < nums2[n_index]:
                nums1[num1_index] = nums2[n_index]
                n_index -= 1
            else:
                nums1[num1_index] = nums1[m_index]
                m_index -= 1
            num1_index -= 1
        nums1[:n_index + 1] = nums2[:n_index + 1]
        return nums1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    nums = solution.merge(nums1, m, nums2, n)
    print(nums)
