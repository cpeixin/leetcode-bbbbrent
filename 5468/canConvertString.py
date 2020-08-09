# coding: utf-8
# Author：Brent
# Date ：2020/8/8 11:12 PM
# Tool ：PyCharm
# Describe ：给你两个字符串 s 和 t ，你的目标是在 k 次操作以内把字符串 s 转变成 t 。
#
# 在第 i 次操作时（1 <= i <= k），你可以选择进行如下操作：
#
# 选择字符串 s 中满足 1 <= j <= s.length 且之前未被选过的任意下标 j （下标从 1 开始），并将此位置的字符切换 i 次。
# 不进行任何操作。
# 切换 1 次字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 'z' 切换后会变成 'a'）。
#
# 请记住任意一个下标 j 最多只能被操作 1 次。
#
# 如果在不超过 k 次操作内可以把字符串 s 转变成 t ，那么请你返回 true ，否则请你返回 false 。
#
#
#
# 示例 1：
#
# 输入：s = "input", t = "ouput", k = 9
# 输出：true
# 解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。


class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t): return False
        char_nums_dict = {'a': 1, 'b': 2, 'c': 3, 'd':4,'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
                          'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,'p':16, 'q':17,
                          'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

        for i in range(len(s)):
            if s[i] != t[i]:
                change_number =  abs(char_nums_dict[t[i]] - char_nums_dict[s[i]]) if char_nums_dict[s[i]] < char_nums_dict[t[i]] else  26 - char_nums_dict[t[i]] + char_nums_dict[s[i]]
                if change_number > k:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    t = "bcd"
    k = 10
    print(solution.canConvertString(s, t, k))