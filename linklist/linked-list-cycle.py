# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False

        fast_node = head.next
        slow_node = head

        while slow_node != fast_node:
            if fast_node is None or fast_node.next is None:
                return False
            fast_node = fast_node.next.next
            slow_node = slow_node.next

        return False