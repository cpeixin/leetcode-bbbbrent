#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 8:53 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : MyHashSet.py
# @Description: 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#
# 实现 MyHashSet 类：
#
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。


class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]