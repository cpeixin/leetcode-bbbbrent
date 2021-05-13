#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 8:28 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : MyHashMap.py
# @Description:不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
#
# 实现 MyHashMap 类：
#
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

"""
链表实现
"""


class Node:

    def __init__(self, key=None, val=None, nex=None):
        self.key = key
        self.val = val
        self.nex = nex


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.h = [Node() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        p = self.h[key % self.size]
        c = p.nex
        while c:
            if c.key == key:
                c.val = value
                break
            p = c
            c = c.nex
        else:
            p.nex = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        c = self.h[key % self.size]
        while c:
            if c.key == key:
                return c.val
            c = c.nex
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        p = self.h[key % self.size]
        c = p.nex
        while c:
            if c.key == key:
                p.nex = c.nex # 移除
                break
            p = c
            c = c.nex


"""不定长数组实现"""


class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hashkey].append([key, value])

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.table[hashkey]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for i, item in enumerate(self.table[hashkey]):
            if item[0] == key:
                self.table[hashkey].pop(i)
                return
