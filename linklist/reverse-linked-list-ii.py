# coding: utf-8
# Author：Brent
# Date ：2020/6/29 4:07 PM
# Tool ：PyCharm
# Describe ：反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return None

    result = ListNode(0)
    result.next = head
    res = result
    for _ in range(m):
        pre = res
        res = res.next

    back = res
    temp1 = None
    temp2 = None
    for _ in range(n - m + 1):
        temp1 = res.next
        res.next = temp2
        temp2 = res
        res = temp1

    pre.next = temp2
    back.next = temp1
    return result.next


if __name__ == '__main__':
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reverseBetween(a, 2, 4)
