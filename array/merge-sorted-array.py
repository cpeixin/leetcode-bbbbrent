# coding: utf-8
# Author：Brent
# Date ：2020/6/13 11:55 AM
# Tool ：PyCharm

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