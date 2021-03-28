# coding: utf-8
# Author：Brent
# Date ：2020/8/7 11:02 PM
# Tool ：PyCharm
# Describe ：给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
#
#  
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/length-of-last-word
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    # def lengthOfLastWord(self, s):
    #     ls = len(s)
    #
    #     # slow and fast pointers
    #     slow = -1
    #     # iterate over trailing spaces
    #     while slow >= -ls and s[slow] == ' ':
    #         slow -= 1
    #     fast = slow
    #     # iterate over last word
    #     while fast >= -ls and s[fast] != ' ':
    #         fast -= 1
    #     return slow - fast
    def lengthOfLastWord(self, s):
        last_word_len = 0
        last_space_flag = True
        for i in range(len(s)-1, -1,-1):
            if s[i] == ' ':
                if not last_space_flag:
                    break
            last_word_len+=1
            last_space_flag = False
        return last_word_len



if __name__ == '__main__':
    solution = Solution()
    str = "hello world"
    print(solution.lengthOfLastWord(str))
