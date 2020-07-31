# coding: utf-8
# Author：Brent
# Date ：2020/7/31 1:53 AM
# Tool ：PyCharm
# Describe ：
import collections


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        num_dict = collections.defaultdict(int)
        not_in_arr2 = []
        result = []
        # 将arr1中元素全部计数到Hash表中
        for num in arr1:
            # 将arr2中没有的元素挑出，并且考虑重复的问题
            if num not in arr2 and num not in not_in_arr2:
                not_in_arr2.append(num)
            num_dict[num] += 1

        # 先遍历arr2，按照Hash表中的value数，拼接结果
        for num in arr2:
            value = num_dict[num]
            result += [num] * value

        # 对arr2中没有出现的元素升序排序
        not_in_arr2.sort()

        # 最后对未出现的元素拼接
        for num in not_in_arr2:
            value = num_dict[num]
            result += [num] * value
        return result


if __name__ == '__main__':
    arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    arr2 = [2, 42, 38, 0, 43, 21]
    solution = Solution()
    result = solution.relativeSortArray(arr1, arr2)
    print(result)

