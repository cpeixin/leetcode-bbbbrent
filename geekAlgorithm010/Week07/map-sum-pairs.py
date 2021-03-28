# coding: utf-8
# Author：Brent
# Date ：2020/7/22 2:23 PM
# Tool ：PyCharm
# Describe ：实现一个 MapSum 类里的两个方法，insert 和 sum。
#
# 对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。
#
# 对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。
#
# 示例 1:
#
# 输入: insert("apple", 3), 输出: Null
# 输入: sum("ap"), 输出: 3
# 输入: insert("app", 2), 输出: Null
# 输入: sum("ap"), 输出: 5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/map-sum-pairs


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for k in key:
            cur = cur.setdefault(k, {})
        cur['v'] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for k in prefix:
            if k not in cur:
                return 0
            cur = cur[k]
        return self.recursive_sum(cur)

    def recursive_sum(self, node):
        value = node.get('v', 0)
        for k in (key for key in node if key != 'v'):
            value += self.recursive_sum(node[k])
        return value


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        for c in key:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['end'] = val

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return 0
            cur = cur[c]
        res = 0
        for key in cur:
            res += self.helper(cur, key)
        return res

    def helper(self, cur, key):
        if key == 'end':
            return cur['end']
        res = 0
        cur = cur[key]
        for key in cur:
            res += self.helper(cur, key)
        return res


if __name__ == '__main__':
    solution = MapSum()
    solution.insert("apple", 3)
    solution.sum("ap")
    solution.insert("app", 2)
    solution.sum("ap")