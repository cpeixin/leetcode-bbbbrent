#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 8:58 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : isValid.py
# @Description:给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        char_dict = {'(': ')', '{': '}', '[': ']', '?': '?'}
        stack = ['?']

        for i in range(len(s)):
            if s[i] not in char_dict:
                if char_dict[stack.pop()] != s[i]: return False
            else:
                stack.append(s[i])
        return len(stack) == 1
