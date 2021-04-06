#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 8:17 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : removeElements.py
# @Description:给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 示例 2：
#
# 输入：head = [], val = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
#
# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/linked-list/f9izv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next
