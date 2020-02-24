class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.Max = k
        self.actLen = 0
        self.front = 0
        self.rear = 1
        self.arr = [0 for i in range(k + 1)]  # 防止一开始front和rear就重叠，所以长度设置为k+1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.actLen += 1
            self.arr[self.front] = value
            self.front = (self.Max + self.front - 1) % self.Max  # TODO: Why?
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.actLen += 1
            self.arr[self.rear] = value
            self.rear = (self.rear + 1) % self.Max
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.actLen -= 1
            self.front = (self.front + 1) % self.Max
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.actLen -= 1
            self.rear = (self.rear - 1) % self.Max
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.arr[(self.front + 1) % self.Max]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.arr[(self.rear - 1) % self.Max]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.actLen <= 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.actLen >= self.Max
