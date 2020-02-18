class circular_queue():
    def __init__(self, size):
        self.array = []
        self.head = 0
        self.tail = 0
        self.size = size

    def enqueue(self, value):
        """入队判满"""
        if (self.tail + 1) % self.size == self.head:
            return False

        self.array.append(value)
        """入队，尾节点下标变化"""
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        """出队判空"""
        if self.head != self.tail:
            item = self.array[self.head]
            """出队，头节点下标变化"""
            self.head = (self.head + 1) % self.size

            return item

if __name__ == '__main__':
    q = circular_queue(5)
    for i in range(5):
        q.enqueue(i)
    q.dequeue()
    q.dequeue()
    q.enqueue(1)
    print(q)