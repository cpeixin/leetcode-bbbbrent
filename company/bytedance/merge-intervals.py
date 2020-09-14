# coding: utf-8
# Author：Brent
# Date ：2020/8/29 9:06 PM
# Tool ：PyCharm
# Describe ：给出一个区间的集合，请合并所有重叠的区间。
#
#
#
# 示例 1:
#
# 输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


class Solution:
    def merger(self, intervals):
        # intervals: List[List[Int]]
        intervals.sort(key = lambda x: x[0])
        res = []
        for array in intervals:
            if not res or res[-1][1] < array[0]:
                res.append(array)
            else:
                res[-1] = [res[-1][0], array[1]]
        return res

if __name__ == '__main__':
    intervals = [[1,3], [2,6],[8,10],[15,18]]
    solution = Solution()
    res = solution.merger(intervals)
    print(res)
