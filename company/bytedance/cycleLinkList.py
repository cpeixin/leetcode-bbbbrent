# coding: utf-8
# Author：Brent
# Date ：2020/8/26 12:37 AM
# Tool ：PyCharm
# Describe ：

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or not head.next: return None
        slow = fast = head
        while True:
            if not fast or not fast.next: return None
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast