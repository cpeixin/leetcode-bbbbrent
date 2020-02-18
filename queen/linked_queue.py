class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node


    def dequeue(self):
        if self.head is None:
            return False

        self.head = self.head.next
        """移除头节点后，如果头节点为空，则尾节点也"""
        if not self.head:
            self.tail = None


if __name__ == '__main__':
    linked_queue = LinkedQueue()

    linked_queue.enqueue(1)
    linked_queue.enqueue(2)
    linked_queue.enqueue(3)

    linked_queue.dequeue()
    linked_queue.dequeue()
    linked_queue.dequeue()
    print(linked_queue.tail)
