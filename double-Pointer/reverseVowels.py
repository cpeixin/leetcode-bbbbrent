#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 6:37 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : reverseVowels.py
# @Description:给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
#
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。
#
#  
#
# 示例 1：
#
# 输入：s = "hello"
# 输出："holle"

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        charList = ['a','e','i','o','u']
        left, right = 0, len(s)-1

        while left < right:
            if s[left] not in charList:
                left += 1
                continue
            if s[right] not in charList:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right-=1
        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    res = solution.reverseVowels(s)
    print(res)
