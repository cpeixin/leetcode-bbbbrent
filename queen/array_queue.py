class ArrayQueue(object):
    def __init__(self, size):
        self.size = size
        self.array = []

        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        """入队判满"""
        if self.tail-self.head+1 == self.size:
            return None
        self.array.append(data)
        self.tail = self.tail + 1

    def dequeue(self):
        """出队判空"""
        if self.tail == self.head:
            return None
        data = self.array[self.head]
        self.head = self.head+1
        return data
