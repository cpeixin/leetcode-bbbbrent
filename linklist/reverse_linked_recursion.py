# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

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
    import sys
    import io
    # def readlines():
    #     for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
    #         yield line.strip('\n')
    #
    # lines = readlines()
    # while True:
    try:
        line = '[1,2,3,4,5]'
        head = stringToListNode(line)
        ret = Solution().reverseList(head)
        out = listNodeToString(ret)
        print(out)
    except StopIteration:
        print("Error")


if __name__ == '__main__':
    main()
