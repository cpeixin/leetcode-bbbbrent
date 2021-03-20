# coding: utf-8
# Author：Brent
# Date ：2020/8/8 10:07 AM
# Tool ：PyCharm
# Describe ：给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#  
#
# 示例:
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-string-ii


class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


if __name__ == '__main__':
    solution = Solution()
    s = "abcdefg"
    k = 2
    res = solution.reverseStr(s, k)
    print(res)