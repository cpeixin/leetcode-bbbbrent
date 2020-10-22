# coding: utf-8
# Author：Brent
# Date ：2020/10/22 9:53 PM
# Tool ：PyCharm
# Describe ：字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。


class Solution:
    def partitionLabels(self, S):
        # 声明哈希字典存储字符出现最远位置
        char_pos = {}
        for i in range(len(S)):
            char_pos[S[i]] = i

        # 定义双指针
        start = 0
        end = 0
        # 记录最远位置
        chr_max_pos = 0

        ans = []
        # 遍历字符串
        while end < len(S):
            # 当前字符出现的最远的位置
            cur_char_max_pos = char_pos[S[end]]
            # 比较，取最远的位置，确保字符被包含在同个片段
            chr_max_pos = max(chr_max_pos, cur_char_max_pos)

            # 如果 end 在最远的位置，表示前面的所有字符都仅出现在这部分，可以切分
            if end == chr_max_pos:
                ans.append(end - start + 1)
                # 更新 start 的位置，查找下一个片段
                start = end + 1

            end += 1

        return ans


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    res = Solution().partitionLabels(S)
    print(res)