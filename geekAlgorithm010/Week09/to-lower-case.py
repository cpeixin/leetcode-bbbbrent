# coding: utf-8
# Author：Brent
# Date ：2020/8/7 10:44 PM
# Tool ：PyCharm
# Describe ：实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
#  
#
# 示例 1：
#
# 输入: "Hello"
# 输出: "hello"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/to-lower-case
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for char in str:
            if char >= 'A' and char <= 'Z':
                char = chr(ord(char) + 32)
            res+=char
        return res