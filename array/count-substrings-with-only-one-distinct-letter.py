# coding: utf-8
# Author：Brent
# Date ：2020/7/12 10:56 AM
# Tool ：PyCharm
# Describe ：



class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        S = S + '!'
        count = 1
        total = 0
        for i in range(len(S) - 1):
            if S[i + 1] != S[i] and S[i] == '1':
                total += (count + 1) * count / 2
                count = 1
            else:
                count += 1
        return total

if __name__ == '__main__':
    solution = Solution()
    print(solution.countLetters("0110111"))