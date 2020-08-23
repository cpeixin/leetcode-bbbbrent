# coding: utf-8
# Author：Brent
# Date ：2020/8/23 10:43 AM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        for i in range(len(strs[0])):
            longest_common = strs[0][i]
            for j in range(1, len(strs)):
                # 此步顺序调换，报错
                if i == len(strs[j]) or strs[j][i] != longest_common:
                    return strs[0][:i]
        return strs[0]
