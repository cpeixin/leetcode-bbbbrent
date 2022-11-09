#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 9:48 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : generateParenthesis.py
# @Description:数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left-1, right)
            if right > left:
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)

