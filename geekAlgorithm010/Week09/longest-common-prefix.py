# coding: utf-8
# Author：Brent
# Date ：2020/8/8 8:53 AM
# Tool ：PyCharm
# Describe ：
from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            common_char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != common_char:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))