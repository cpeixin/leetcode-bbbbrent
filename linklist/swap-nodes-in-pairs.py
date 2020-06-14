# coding: utf-8
# Author：Brent
# Date ：2020/6/14 11:44 AM
# Tool ：PyCharm
# Describe ：给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果没有节点或者只有一个head节点
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next
        # 指向下个相邻节点交换后的头节点
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        # 返回每次交换的头节点
        return second_node