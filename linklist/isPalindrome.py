#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 8:51 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : isPalindrome.py
# @Description:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否是回文
        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        # 恢复链表
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    # 确定中间节点
    def end_of_first_half(self, head):
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        pre = None
        curr = head
        while curr is not None:
            nextnode = curr.next
            curr.next = pre
            pre = curr
            curr = nextnode
        return pre
