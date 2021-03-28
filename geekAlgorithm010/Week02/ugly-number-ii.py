# coding: utf-8
# Author：Brent
# Date ：2020/6/19 9:20 AM
# Tool ：PyCharm
# Describe ：我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#  
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
#
# 1 是丑数。
# n 不超过1690。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/chou-shu-lcof
import heapq

def nthUglyNumber(n: int) -> int:

    heap = [1]
    heapq.heapify(heap)
    res = 0
    for _ in range(n):
        res = heapq.heappop(heap)
        while heap and res == heap[0]:
            res = heapq.heappop(heap)
        a, b, c = res * 2, res * 3, res * 5
        for t in [a, b, c]:
            heapq.heappush(heap, t)
    return res

def nthUglyNumber_1(n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]

        curr_ugly = 1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = curr_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return curr_ugly


if __name__ == '__main__':
    nthUglyNumber_1(10)