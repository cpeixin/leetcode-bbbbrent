# coding: utf-8
# Team : Quality Management Center
# Author：Brent
# Date ：2020/6/13 2:27 PM
# Tool ：PyCharm
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 递归条件
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
