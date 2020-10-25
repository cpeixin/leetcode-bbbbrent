# coding: utf-8
# Author：Brent
# Date ：2020/10/25 2:14 PM
# Tool ：PyCharm
# Describe ：我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
#
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
#
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
#
# 如果不含有 “山脉” 则返回 0。


from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                if right < n - 1 and A[right] > A[right + 1]:
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans


if __name__ == '__main__':
    array = [2, 1, 4, 7, 3, 2, 5]
    solution = Solution()
    res = solution.longestMountain(array)
    print(res)
