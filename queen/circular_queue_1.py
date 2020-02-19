class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k+1
        self.queue = []
        self.head = 0
        self.tail = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        """判断队满"""
        if (self.tail + 1) % self.size == self.head:
            return False
        self.queue.append(value)
        self.tail = (self.tail + 1) % self.size
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        """出队判空"""
        if self.tail == self.head:
            return False
        self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.head != self.tail:
            return self.queue[self.head]
        return False

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.head != self.tail:
            return self.queue[self.tail-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.queue:
            return False
        return True

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (self.tail + 1) % self.size == self.head:
            return True
        return False


if __name__ == '__main__':
    """
["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
[[6],[6],[],[],[],[5],[],[],[],[],[],[]]
"""
    circularQueue = MyCircularQueue(6)

    circularQueue.enQueue(6)

    circularQueue.Rear()

    circularQueue.Rear()

    circularQueue.deQueue()

    circularQueue.enQueue(5)

    circularQueue.Rear()

    circularQueue.deQueue()

    tmp = circularQueue.Front()

    circularQueue.deQueue()

    circularQueue.deQueue()

    circularQueue.deQueue()

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
