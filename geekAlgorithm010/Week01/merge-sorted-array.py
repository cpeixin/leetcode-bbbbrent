# coding: utf-8
# Author：Brent
# Date ：2020/6/13 4:14 PM
# Tool ：PyCharm
# Describe ：给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#  
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m_index, n_index, num1_index = m-1, n-1, m+n-1
        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] < nums2[n_index]:
                nums1[num1_index] = nums2[n_index]
                n_index-=1
            else:
                nums1[num1_index] = nums1[m_index]
                m_index-=1

            num1_index-=1
        # 防止nums1为空或者m<n的情况
        nums1[:n_index+1] = nums2[:n_index+1]