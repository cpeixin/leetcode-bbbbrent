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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = [beginWord]
        # queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)
        step = 1
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        while queue:
            # current_size = len(queue)
            for i in range(len(queue)):
                word = queue.pop(0)

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in tmp:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0

    def ladderLength_1(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        length = len(beginWord)
        wordSet = set(wordList)

        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for cur in head:
                for i in range(length):
                    for j in tmp:
                        word = cur[:i] + j + cur[i + 1:]

                        if word in tail:
                            return res + 1
                        if word in wordSet:
                            q.add(word)
                            wordSet.remove(word)
            head = q
            res += 1

        return 0

    def ladderLength_2(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if endWord not in word_set or len(word_set) == 0: return 0
        if beginWord in word_set: word_set.remove(beginWord)
        queue = [beginWord]
        word_len = len(beginWord)
        visited_word = set(beginWord)
        step = 1
        tmp_char = list('abcdefghijklmnopqrstuvwxyz')
        while queue:
            for _ in range(len(queue)):
                word = queue.pop(0)
                wordIter = list(word)
                for index in range(word_len):
                    original_char = wordIter[index]
                    for char in tmp_char:
                        wordIter[index] = char
                        next_word = ''.join(wordIter)
                        if next_word in word_set:
                            if next_word == endWord: return step + 1
                            if next_word not in visited_word:
                                queue.append(next_word)
                                visited_word.add(next_word)
                    wordIter[index] = original_char
            step += 1

        return 0


if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "ymain"
    endWord = "oecij"
    wordList = ["ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij", "xecij", "yecij", "ymanj", "yzcnj", "ymain"]

    solution = Solution()
    res = solution.ladderLength_2(beginWord, endWord, wordList)
    print(res)
