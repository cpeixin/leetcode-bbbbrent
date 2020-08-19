# coding: utf-8
# Author：Brent
# Date ：2020/8/10 7:11 PM
# Tool ：PyCharm
# Describe ：假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        begin = 0
        end = len(nums)-1
        while begin<=end:
            mid = begin+(end-begin)//2
            # 找到目标值了直接返回
            if nums[mid]==target:
                return mid
            # 如果左侧是有序的
            if nums[begin]<=nums[mid]:
                # 同时target在[ nums[begin],nums[mid] ]中
                # 那么就在这段有序区间查找
                if nums[begin]<=target<=nums[mid]:
                    end = mid-1
                # 否则去反方向查找
                else:
                    begin = mid+1
            # 如果右侧是有序的
            else:
                # 同时target在 ( nums[mid],nums[end] ]中
                # 那么就在这段有序区间查找
                if nums[mid]<target<=nums[end]:
                    begin = mid+1
                # 否则去反方向查找
                else:
                    end = mid-1
        return -1