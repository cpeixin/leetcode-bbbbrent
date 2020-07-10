# Definition for singly-linked list.
"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None: return False

        fast_node = head.next
        slow_node = head

        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None:
                return False
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return False