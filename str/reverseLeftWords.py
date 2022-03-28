'''
Author: your name
Date: 2021-10-02 09:56:02
LastEditTime: 2022-03-14 17:01:54
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode-bbbbrent/str/reverseLeftWords.py
'''
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

#  

# 示例 1：

# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
# 示例 2：

# 输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """切片方法"""
        return s[n:] + s[:n]
        """列表遍历"""
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)
        """自己实现三段反转"""
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        
        res = list(s)
        end = len(res) - 1
        reverse_sub(res, 0, n - 1)
        reverse_sub(res, n, end)
        reverse_sub(res, 0, end)
        return ''.join(res)