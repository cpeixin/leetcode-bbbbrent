# coding: utf-8
# Author：Brent
# Date ：2020/9/14 1:06 PM
# Tool ：PyCharm
# Describe ：

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 二分查找
        # x是否可能为乘法表中第k小的数
        def Valid(x):
            ans = 0
            # 遍历每一行,对于第i行,如果存在k * i <= x此时k <= x // i,即比x小的数最多为k个
            # 如果不存在,则整行数都比x小
            for i in range(1, m + 1):
                ans += min(x // i, n)
            return ans >= k

        l, r = 1, m * n
        while l <= r:
            mid = l + (r - l) // 2
            if Valid(mid):
                r = mid - 1
            else:
                l = mid + 1
                # 返回最后的合理值
        return r + 1



if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthNumber(3, 3, 4))