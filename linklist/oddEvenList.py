#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 8:12 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : oddEvenList.py
# @Description:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        evenHead = head.next
        odd, even = head, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head