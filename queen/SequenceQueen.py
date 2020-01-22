class SequenceQueen:
    """
    Sequential Queue implement
    """

    def __init__(self):
        """
        initialize an empty Queue, __queue means it's a private member
        """
        self.__queue = []

    def first(self):
        """
        get the first element of Queue
        :return: if Queue is empty return None, else return the first element
        """
        return None if self.isEmpty() else self.__queue[0]

    def enqueue(self, obj):
        """
        enqueue an element into Queue
        :param obj: object to be enqueued
        """
        self.__queue.append(obj)

    def dequeue(self):
        """
        dequeue the first element from Queue
        :return: if Queue is empty return None, else return the dequeued element
        """
        return None if self.isEmpty() else self.__queue.pop(0)

    def clear(self):
        """
        clear the whole Queue
        """
        self.__queue.clear()

    def isEmpty(self):
        """
        judge the Queue is empty or not
        :return: bool value
        """
        return self.length() == 0

    def length(self):
        """
        get the length of Queue
        :return:
        """
        return len(self.__queue)


obj_queen = SequenceQueen()

obj_queen.enqueue(10)
obj_queen.enqueue(9)
obj_queen.enqueue(8)

obj_queen.dequeue()

print(obj_queen.first())
print(obj_queen.length())
