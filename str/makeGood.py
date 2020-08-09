# coding: utf-8
# Author：Brent
# Date ：2020/8/9 11:02 AM
# Tool ：PyCharm
# Describe ：给你一个由大小写英文字母组成的字符串 s 。
#
# 一个整理好的字符串中，两个相邻字符 s[i] 和 s[i + 1] 不会同时满足下述条件：
#
# 0 <= i <= s.length - 2
# s[i] 是小写字符，但 s[i + 1] 是对应的大写字符；反之亦然 。
# 请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。
#
# 请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。
#
# 注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if not s or (len(s) == 1 and s[0] not in upper_char): return s

        slow, fast = 0, 1
        s_list = list(s)
        while fast <= len(s_list)-1:
            if (s_list[fast] in upper_char and s_list[slow] not in upper_char) or (s_list[fast] not in upper_char and s_list[slow] in upper_char):
                s_list.pop(slow)
                s_list.pop(slow)
                slow = 0
                fast = 1
                # s_list.pop(fast)
            else:
                slow+=1
                fast+=1
        return ''.join(s_list)


if __name__ == '__main__':
    s = "s"
    solution = Solution()
    print(solution.makeGood(s))


