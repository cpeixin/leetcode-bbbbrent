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
        node = self.head

        while node.data != value and node is not None:
            node = node.next_node

        return node

    def find_by_index(self, index):
        # if index is None or self.head is None:
        #     return

        flag = 1

        node = self.head

        while flag != index and node is not None:
            node = node.next_node
            flag += 1

        return node

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
        """在链表的某个指定Node节点之前插入一个存储value数据的Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新的Node节点中的数据
        """
        if (node is None) or (self.head is None):  # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
            return

        if node == self.head:  # 如果是在链表头之前插入数据节点，则直接插入
            self.insert_to_head(data)
            return

        new_node = Node(data)
        pro = self.head
        not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        while pro.next_node != node:  # 寻找指定Node之前的一个Node
            if pro.next_node is None:  # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def insert_after(self,node, data):
        # """在链表的某个指定Node节点之后插入一个存储value数据的Node节点.
        # 参数:
        #     node:指定的一个Node节点
        #     value:将要存储在新Node节点中的数据
        # """

        """first"""

        if node is None:  # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(data)
        """这里没有判断指定的节点是否存在，是因为可以直接使用"""
        new_node.next_node = node.next
        node.next = new_node


        # if (node is None) or (self.head is None):  # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
        #     return
        #
        # new_node = Node(data)
        #
        # if node == self.head:  # 如果是在链表头之前插入数据节点，则直接插入
        #     new_node.next_node = node.next_node
        #     self.head.next_node = new_node
        #
        # else:
        #     pro = self.head
        #     not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        #     while pro.next_node != node:  # 寻找指定Node之前的一个Node
        #         if pro.next_node is None:  # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
        #             not_found = True
        #             break
        #         else:
        #             pro = pro.next_node
        #     if not not_found:
        #         new_node.next_node = pro.next_node
        #         pro.next_node = new_node

    def delete_by_node(self,node):
        """在链表中删除指定Node的节点.
           参数:
               node:指定的Node节点
        """
        if self.head is None:  # 如果链表是空的，则什么都不做
            return

        if node == self.head:  # 如果指定删除的Node节点是链表的头节点
            self.head = node.next_node
            return

        pro = self.head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next_node != node:
            """如果没有这个节点，则最后回死在这个if条件中，break出去"""
            if pro.next_node is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node

    def delete_by_value(self, value):
        """在链表中删除指定存储数据的Node节点.
                参数:
                    value:指定的存储数据
                """
        if self.head is None:  # 如果链表是空的，则什么都不做
            return

        if self.head.data == value:  # 如果链表的头Node节点就是指定删除的Node节点
            self.head = self.head.next_node
            return

        pro = self.head
        node = self.head.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到执行Value值的Node节点
                not_found = True
                break
            else:
                pro = node
                node = node.next_node
        if not_found is False:
            pro.next_node = node.next_node

    def foeach(self, node):
        """遍历链表"""
        while node != None:
            print(node.data, node.next_node)
            node = node.next_node




if __name__ == '__main__':
    sll = SinglyLinkedList()

    for i in range(10):
        sll.insert_to_head(i)

    sll.foeach(sll.head)

    # node_5 = sll.find_by_value(5)
    # sll.insert_after(node_5,5.5)


    # sll.insert_to_tail(100)
    # print(sll.tail.data)


    # node_8 = sll.find_by_value(8)
    # print("================")
    # print(node_8)


    # node_index_3 = sll.find_by_index(3)
    # print("================")
    # print(node_index_3)


    # sll.delete_by_value(9)