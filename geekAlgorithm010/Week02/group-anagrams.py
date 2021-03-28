# coding: utf-8
# Author：Brent
# Date ：2020/6/15 2:59 PM
# Tool ：PyCharm
# Describe ：给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#

# 链接：https://leetcode-cn.com/problems/group-anagrams
import collections


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    dict = collections.defaultdict(list)
    for str in strs:
        dict[tuple(sorted(str))].append(str)
    return dict.values()



if __name__ == '__main__':
    s = "[\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"]"
    groupAnagrams(s)