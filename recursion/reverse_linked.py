"""

假设列表为：n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

若从节点 nk+1 到 nm 已经被反转，而我们正处于 nk。

n1 → … → nk-1 → nk → nk+1 ← … ← nm

我们希望 nk+1 的下一个节点指向 nk。

所以，

nk.next.next = nk;

要小心的是 n1 的下一个必须指向 Ø 。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return p
