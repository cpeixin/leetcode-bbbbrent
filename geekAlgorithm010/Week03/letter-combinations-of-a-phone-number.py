# coding: utf-8
# Author：Brent
# Date ：2020/6/27 11:09 AM
# Tool ：PyCharm
# Describe ：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    map_ = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []
    def make_combinations(i, cur):
        if i == len(digits):
            if len(cur) > 0:
                result.append(''.join(cur))
            return
        for ch in map_[digits[i]]:
            cur.append(ch)
            make_combinations(i + 1, cur)
            cur.pop()
    make_combinations(0, [])
    return result

if __name__ == '__main__':
    result = letterCombinations("23")
    print(result)