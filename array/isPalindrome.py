'''
Author: your name
Date: 2022-03-14 17:40:07
LastEditTime: 2022-03-14 18:12:41
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 说明： 本题中，我们将空字符串定义为有效的回文串。 
示例 1: 输入: A man, a plan, a canal: Panama
输出: true
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower:
                return False
            left += 1
            right -= 1
 

        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    print(res)