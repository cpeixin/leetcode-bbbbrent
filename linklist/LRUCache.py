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
        self.tail.pre = self.top

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        """判断节点是否存在"""
        if key in self.catche.keys():
            cur = self.catche[key]

            """首先跳出原来的位置，"""









    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
