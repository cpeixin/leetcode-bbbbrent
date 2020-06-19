# coding: utf-8
# Author：Brent
# Date ：2020/6/19 4:23 PM
# Tool ：PyCharm
# Describe ：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-palindrome
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def isPalindrome(self, s):
        str = "".join(char.lower() for char in s if char.isalnum())
        n = len(str)
        left, right = 0, n-1
        while left < right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1
        return True