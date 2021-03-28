#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 9:45 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : twoSum.py
# @Description:给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
#
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
#
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

class Solution:
    def twoSum(self, numbers, target):
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]