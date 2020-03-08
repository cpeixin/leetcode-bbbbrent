# Definition for singly-linked list.
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # maintain an unchanging reference to node ahead of the return node.
        # prehead 哨兵节点
        prehead = ListNode(-1)
        # 维护一个前置节点
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    #
    # lines = readlines()
    # while True:
    #     try:
    #
    #
    #         # line = lines.next()
    l1 = stringToListNode('[1, 2, 4]')
            # line = lines.next()
    l2 = stringToListNode('[1, 3, 4]')

    ret = Solution().mergeTwoLists(l1, l2)

    out = listNodeToString(ret)
    print(out)
        # except StopIteration:
        #     break


if __name__ == '__main__':
    main()