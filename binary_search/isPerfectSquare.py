# coding: utf-8
# Author：Brent
# Date ：2020/7/5 11:48 PM
# Tool ：PyCharm
# Describe ：


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if num < 2:
        #     return True

        left, right = 0, num

        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1

        return False

if __name__ == '__main__':
    solution = Solution()
    result = solution.isPerfectSquare(14)
    print(result)