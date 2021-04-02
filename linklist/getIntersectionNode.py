#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 8:42 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : getIntersectionNode.py
# @Description:编写一个程序，找到两个单链表相交的起始节点。
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
