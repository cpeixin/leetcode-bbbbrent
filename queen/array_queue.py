from typing import Optional
class ArrayQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: int) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0

        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head: self._tail])

if __name__ == '__main__':
    array_queue = ArrayQueue(5)
    array_queue.enqueue(1)
    array_queue.enqueue(2)
    array_queue.enqueue(3)
    array_queue.enqueue(4)
    array_queue.enqueue(5)
    # array_queue.enqueue(6)


    print(array_queue._head)
    print(array_queue._tail)