# coding: utf-8
# Author：Brent
# Date ：2020/8/1 12:32 AM
# Tool ：PyCharm
# Describe ：运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#  
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.size > 0:
                self.size -= 1
            else:
                self.cache.popitem(last = False)
        self.cache[key] = value


