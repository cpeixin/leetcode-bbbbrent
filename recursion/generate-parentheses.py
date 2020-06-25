# coding: utf-8
# Author：Brent
# Date ：2020/6/23 9:01 PM
# Tool ：PyCharm
# Describe ：数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
#
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
def generateParenthesis(n):
    def generate(str, left, right, array=[]):
        if left: generate(str+'(', left-1, right)
        if right>left: generate(str+')', left, right-1)
        if not right: array+=str,
        return array
    return generate('', n, n)

if __name__ == '__main__':
    result = generateParenthesis(3)
    print(result)