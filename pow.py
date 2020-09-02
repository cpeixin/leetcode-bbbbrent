# coding: utf-8
# Author：Brent
# Date ：2020/9/1 3:40 PM
# Tool ：PyCharm
# Describe ：
#
#
# 当 nn 为奇数时，二分后会多出一项 xx
# 根据推导，可通过循环 x = x^2x=x
# 2
#   操作，每次把幂从 nn 降至 n//2n//2 ，直至将幂降为 00 ；
# 设 res=1res=1 ，则初始状态 x^n = x^n \times resx
# n
#  =x
# n
#  ×res 。在循环二分时，每当 nn 为奇数时，将多出的一项 xx 乘入 resres ，则最终可化至 x^n = x^0 \times res = resx
# n
#  =x
# 0
#  ×res=res ，返回 resres 即可。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

if __name__ == '__main__':
    solution = Solution()
    x = 2.00000
    n  = 10
    result = solution.myPow(x, n)
    print(result)