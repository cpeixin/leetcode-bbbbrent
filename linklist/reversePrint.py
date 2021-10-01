'''
Author: your name
Date: 2021-10-01 08:57:18
LastEditTime: 2021-10-01 08:58:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-bbbbrent/linklist/reversePrint.py
'''

"""辅助栈"""
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head: return []
        stack = []
        res = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res