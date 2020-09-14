# coding: utf-8
# Author：Brent
# Date ：2020/8/24 11:18 AM
# Tool ：PyCharm
# Describe ：运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？



class Node:
    def __init__(self,key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head


    def put(self, key, value):
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.size += 1
            self.add_to_head(node)
            if self.size > self.capacity:
                tail = self.remove_tail()
                self.size -= 1
                self.cache.pop(tail.key)
        else:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)


    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            value = node.value
            self.move_to_head(node)
            return value


    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.pre = node

        node.pre = self.head
        self.head.next = node



    def remove_tail(self):
        node = self.tail.pre
        self.remove_node(node)
        return node

