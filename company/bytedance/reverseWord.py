# coding: utf-8
# Author：Brent
# Date ：2020/8/23 3:08 PM
# Tool ：PyCharm
# Describe ：
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == '': return ''
        s = s.strip()
        ans = []
        left, right = len(s)-1, len(s)-1
        # for left in range(len(s)-1, -1, -1):
        while left >= 0:
            while left >= 0 and s[left] != ' ':
                left -= 1
            ans.append(s[left+1:right+1])
            while left >= 0 and s[left] == ' ':
                left -= 1
            right = left
        return ' '.join(ans)