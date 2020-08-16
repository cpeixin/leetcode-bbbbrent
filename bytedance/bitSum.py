# coding: utf-8
# Author：Brent
# Date ：2020/8/9 8:24 PM
# Tool ：PyCharm
# Describe ：62进制加法

class Solution:
    def bitSum(self, str1, str2):
        # 初始化dict
        bit_dict = {}
        for i in range(10):
            bit_dict[str(i)] = i
        for i in range(0,26):
            char = ord('a') + i
            bit_dict[chr(char)] = i + 10
        for i in range(0,26):
            char = ord('A') + i
            bit_dict[chr(char)] = i + 36

        str1_list = list(str1)
        str2_list = list(str2)

        str1_list_len, str2_list_len = len(str1_list)-1, len(str2_list)-1

        while str1_list_len > 0 and str2_list_len > 0:
            return ''


if __name__ == '__main__':
    solution = Solution()
    solution.bitSum('aaaa','cccc')