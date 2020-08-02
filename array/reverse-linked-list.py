# coding: utf-8
# Author：Brent
# Date ：2020/8/2 3:19 PM
# Tool ：PyCharm
# Describe ：反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        pre = None
        curr = head
        while head:
            head = curr.next
            curr.next = pre
            pre = curr
        return pre