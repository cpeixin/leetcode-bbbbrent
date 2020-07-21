# coding: utf-8
# Author：Brent
# Date ：2020/6/29 10:58 PM
# Tool ：PyCharm
# Describe ：给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-ladder

from typing import List
from collections import deque


class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        import collections
        if endWord not in wordList or len(wordList) == 0: return 0
        wordList = set(wordList)
        # 这道题是让求解 ”转换序列的长度，而不是求转换的次数，所以length初始长度设置为1“
        queue = collections.deque([(beginWord, 1)])
        while queue:
            cur_word, length = queue.popleft()
            if cur_word == endWord: return length
            # 不存在
            for index in range(len(cur_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = cur_word[:index] + char + cur_word[index + 1:]
                    if new_word in wordList:
                        queue.append((new_word, length + 1))
                        wordList.remove(new_word)
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "ymain"
    # endWord = "oecij"
    # wordList = ["ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain"]

    solution = Solution()
    res = solution.ladderLength_3(beginWord, endWord, wordList)
    print(res)
