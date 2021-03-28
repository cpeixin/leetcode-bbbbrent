#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 9:10 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : arrayPairSum.py
# @Description:给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
#
# 返回该 最大总和 。

class Solution:
    def arrayPairSum(self, nums):
        nums.sort() # 排序
        result = 0
        for i in range(0, len(nums), 2) : # 每间隔2个单位，取一个数值相加
            result += nums[i]
        return result