#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 11:57 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : firstUniqChar.py
# @Description:给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#  
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/hash-table/xxx94s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        charIndexMap = {}

        for i, ch in enumerate(s):
            if ch not in charIndexMap:
                charIndexMap[ch] = 1
            else:
                charIndexMap[ch] += 1

        for key, value in charIndexMap.items():
            if value == 1:
                return s.index(key)


if __name__ == '__main__':
    s = "leetcode"
    a = Solution().firstUniqChar(s)
    print(a)
