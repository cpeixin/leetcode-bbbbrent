#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 11:00 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : reverseOnlyLetters.py
# @Description:给你一个字符串 s ，根据下述规则反转字符串：
#
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。
#
#  
#
# 示例 1：
#
# 输入：s = "ab-cd"
# 输出："dc-ba"
# 示例 2：
#
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 示例 3：
#
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        length = len(s)
        left, right = 0, length - 1
        sList = list(s)
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            if left < right:
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
        return "".join(sList)


if __name__ == '__main__':
    solution = Solution()
    s = "Test1ng-Leet=code-Q!"
    res = solution.reverseOnlyLetters(s)
    print(res)

