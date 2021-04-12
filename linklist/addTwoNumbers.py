#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 8:38 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : addTwoNumbers.py
# @Description:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):  # 定义两数相加函数
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 如果有一个链表为空，返回另外一个
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # tmp是暂存（temporal）
        tmp = ListNode(0)  # 引用ListNode类定义了一个链表节点并赋给tmp
        # res是重置（reset）
        res = tmp  # 赋值
        # flag 标示
        flag = 0  # 初始化
        while l1 or l2:  # l1或l2不为空就持续执行
            tmp_sum = 0  # 链表节点值的和
            if l1:  # 如果l1不为空，把l1的某个节点值的和赋给tmp_sum
                tmp_sum = l1.val  # 把l1的某个节点的值赋给tmp_sum
                l1 = l1.next
            if l2:  # 如果l2不为空，把l2中和l1对应的节点的值加到tmp_sum
                tmp_sum += l2.val
                l2 = l2.next  # 指向下一个节点，为下一次的加和做准备
            tmp_res = ((tmp_sum + flag) % 10)  # 个位数字
            flag = ((tmp_sum + flag) // 10)  # 进位的数
            res.next = ListNode(tmp_res)
            res = res.next  # res后移
            if flag:  # 如果flag不为0，就是对应位置相加后有进位
                res.next = ListNode(1)  # res的下一节点设为1
        res = tmp.next  # 赋值
        del tmp  # 删除tmp变量
        return res  # 返回res链表