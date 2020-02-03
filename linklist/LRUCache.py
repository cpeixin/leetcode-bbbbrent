"""
https://github.com/wangzheng0822/algo/blob/master/python/06_linkedlist/LRUCache.py
"""
class DbListNode(object):
    def __init__(self, x, y):
        """
        节点为哈希表+双向链表
        :param x:
        :param y:
        """
        self.key = x
        self.value = y

        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        初始化一个空双向链表
        :type capacity: int
        """

        self.cap = capacity
        self.catche = {}

        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)

        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        """判断节点是否存在"""
        if key in self.catche.keys():
            cur = self.catche[key]

            """首先跳出原来的位置"""
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            """top,tail为哨兵节点"""
            top_node = self.top.next
            cur.next = top_node

            top_node.prev = cur


            self.top.next = cur
            cur.prev = self.top

            return cur.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.catche.keys():
            """如果插入节点存在，则将插入节点调换为位，插入到哨兵节点后的头节点。此时不存在增删节点，所以不用判断链表长度"""
            cur = self.catche[key]

            """首先跳出原来的位置"""
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            """top,tail为哨兵节点"""
            top_node = self.top.next
            cur.next = top_node

            top_node.prev = cur


            self.top.next = cur
            cur.prev = self.top

        else:
            # 增加新结点至首部
            cur = DbListNode(key, value)
            self.catche[key] = cur
            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            """判断长度删除尾节点"""
            if len(self.catche.keys()) > self.cap:
                self.catche.pop(self.tail.prev.key)
                # 去掉原尾结点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.value))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    print(cache)
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    print(cache)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)