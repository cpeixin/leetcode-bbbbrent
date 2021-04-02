#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 9:14 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : removeNthFromEnd.py
# @Description:给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
# 进阶：你能尝试使用一趟扫描实现吗？

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentryNode = ListNode(0)
        sentryNode.next = head

        slow = fast = sentryNode

        for _ in range(n):
            fast = fast.next

        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next

        # 此时slow节点在倒数n节点的前一个节点
        slow.next = slow.next.next
        return sentryNode.next