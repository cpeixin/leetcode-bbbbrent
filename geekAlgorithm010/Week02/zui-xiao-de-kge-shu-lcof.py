# coding: utf-8
# Author：Brent
# Date ：2020/6/17 3:56 PM
# Tool ：PyCharm
# Describe ：输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#  
#
# 示例 1：
#
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#  
#
# 限制：
#
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof


import heapq


def getLeastNumbers(arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0: return list()
        hp = [-elem for elem in arr[:k]]
        # 如果不利用相反数，则[3,2,1]返回的是【1，3】
        heapq.heapify(hp)
        for index in range(k, len(arr)):
            if arr[index] < -hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[index])

        result = [-elem for elem in hp]
        return result


if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    result = getLeastNumbers(arr, k)
    print(result)