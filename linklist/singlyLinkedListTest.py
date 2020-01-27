# 1.单链表的插入、删除、查找操作；
# 2.链表中存储的数据类型是Int
#
# Author:Brent


class Node(object):

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node


class SinglyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_head(self, data):
        """
        next_node为None注意
        :param data:
        :param next_node:
        """
        node = Node(data)
        node.next_node = self.head

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head = node

    def insert_to_tail(self,data):
        """
        尾节点插入
        :param data:
        """
        if self.head is None:
            self.insert_to_head(data)
        else:
            node = Node(data)
            node.next_node = None
            self.tail.next_node = node
            self.tail = node

if __name__ == '__main__':
    sll = SinglyLinkedList()

    for i in range(10):
        sll.insert_to_head(i)
    sll.insert_to_tail(100)
    print(sll)
    print(sll.head.data)
    print(sll.tail.data)