# coding: utf-8
# Author：Brent
# Date ：2020/10/21 11:40 PM
# Tool ：PyCharm
# Describe ：你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed: return True
        if not name or not typed: return False
        if name[0] != typed[0]: return False
        name_len = len(name)
        typed_len = len(typed)
        i = 0
        j = 0
        while i < name_len:
            if j >= typed_len: return False
            name_char = name[i]
            typed_char = typed[j]

            if name_char == typed_char:
                i += 1
                j += 1
            elif name_char != typed_char and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return True



if __name__ == '__main__':
    name = "alex"
    typed = "alexxr"

    res = Solution().isLongPressedName(name, typed)
    print(res)
