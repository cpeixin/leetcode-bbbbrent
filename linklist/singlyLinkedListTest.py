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


    def find_by_value(self, value):
        if value is None or self.head is None:
            return

        offset = self.head

        while offset.data != value:
            offset = offset.next_node

        return offset


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

    def insert_before(self, node, data):
        if node is None or self.head is None:
            return

        if node==self.head:
            self.insert_to_head(data)
            return

        """从头节点遍历"""
        new_node = Node(data)
        offset = self.head
        not_found = False

        while offset.next_node != node:
            offset = offset.next_node


        new_node.next_node = offset.next_node

        offset.next_node = new_node

    def foeach(self, node):
        """遍历链表"""
        while node.next_node != None and node != None:
            node = node.next_node
            print(node.data, node.next_node)

if __name__ == '__main__':
    sll = SinglyLinkedList()

    for i in range(10):
        sll.insert_to_head(i)
    sll.insert_to_tail(100)

    sll.foeach(sll.head)

    node_8 = sll.find_by_value(8)
    # print(sll)
    # print(sll.head.data)
    # print(sll.tail.data)

    print(node_8)