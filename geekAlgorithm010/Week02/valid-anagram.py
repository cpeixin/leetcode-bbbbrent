# coding: utf-8
# Author：Brent
# Date ：2020/6/15 12:38 PM
# Tool ：PyCharm
# Describe ：给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false

# 链接：https://leetcode-cn.com/problems/valid-anagram
import collections


def isAnagram_1(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    char_dict = {}

    for index in range(len(s)):
        if s[index] in char_dict:
            char_dict[s[index]] += 1
        else:
            char_dict[s[index]] = 1
    for index in range(len(t)):
        if t[index] in char_dict:
            char_dict[t[index]] -= 1
        else:
            char_dict[t[index]] = 1
    for char in char_dict.keys():
        if char_dict[char] != 0:
            return False
    return True

def isAnagram_2(s, t):
    return sorted(s) == sorted(t)


def isAnagram_3(s, t):
    return collections.Counter(s) == collections.Counter(t)

def isAnagram_4(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # defaultdict
    if len(s) != len(t):
        return False

    dict = collections.defaultdict(int)
    for index in range(len(s)):
        dict[s[index]] += 1
        dict[t[index]] -= 1
    for value in dict.values():
        if value != 0:
            return False
    return True




if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    # isAnagram(s, t)
    isAnagram_1(s, t)
