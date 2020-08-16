# coding: utf-8
# Author：Brent
# Date ：2020/8/16 4:43 PM
# Tool ：PyCharm
# Describe ：

class Solution(object):
    def ladderLength(self,beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        queue = [(beginWord, 1)]

        char_list = 'abcdefghijklmnopqrstuvwxyz'
        while queue:
            current_word, length = queue.pop(0)
            if current_word == endWord: return length
            for index in range(len(current_word)):
                for char in char_list:
                    new_word = current_word[:index] + char + current_word[index+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append((new_word, length+1))
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)


