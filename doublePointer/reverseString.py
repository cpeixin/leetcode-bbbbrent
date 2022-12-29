#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 6:06 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : reverseString.py
# @Description:编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
#  
#
# 示例 1：
#
# 输入：s = ["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：
#
# 输入：s = ["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 0: return s

        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    res = solution.reverseString(s)
    print(res)
