# coding: utf-8
# Author：Brent
# Date ：2020/9/13 1:29 PM
# Tool ：PyCharm
# Describe ：给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board, word):


        rows = len(board)
        columns = len(board[0])

        mark = [[0 * columns] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1: ]) == True:
                        return True
                    else:
                        mark[i][j] = 0

        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0: return True
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]

            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                if mark[cur_i][cur_j] == 1:
                    continue
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]) == True:
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
            return False