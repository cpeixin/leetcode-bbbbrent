# coding: utf-8
# Author：Brent
# Date ：2020/8/8 11:44 AM
# Tool ：PyCharm
# Describe ：给定一个字符串，逐个翻转字符串中的每个单词。
#
#  
#
# 示例 1：
#
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例 2：
#
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 示例 3：
#
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def reverseWords(self, s):
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回


if __name__ == '__main__':
    s = ' hello world  '
    solution = Solution()
    str = solution.reverseWords(s)
    print(str)

