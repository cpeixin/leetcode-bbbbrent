# coding: utf-8
# Author：Brent
# Date ：2020/7/6 6:58 PM
# Tool ：PyCharm
# Describe ：给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。
#
# 示例：
#
# 输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sub-sort-lcci



class Solution:
    def subSort(self, array):
        #  定义max, min变量需要注意，因为是一次遍历，双向执行，所以max，min变量初始值则为最小，最大数
        max_num, min_num = float('-inf'), float('inf')
        left_index, right_index = -1, -1
        for index in range(len(array)):
            # 这一步可以理解为，从前向后遍历，最后一个 array[i] < array[i-1]
            if array[index] < max_num: right_index = index
            else: max_num = array[index]
            # 这一步则是从后向前遍历，找到最后一个 array[i] > array[i+1]的元素
            if array[len(array)-1-index] > min_num: left_index = len(array)-1-index
            else: min_num = array[len(array)-1-index]
        return [left_index, right_index]

if __name__ == '__main__':
    solution = Solution()
    result = solution.subSort([1,2,4,7,10,11,7,12,6,7,16,18,19])
    print(result)