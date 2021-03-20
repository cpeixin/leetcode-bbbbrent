#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


class BinarySearchTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def findelem(self, value, node, parent, nodetype):
        """查找一个值"""
        if node == None:
            return False, node, parent, nodetype
        elif node.value == value:
            return True, node, parent, nodetype
        elif value < node.value:
            return self.findelem(value, node.lchild, node, 'lchild')
        elif value > node.value:
            return self.findelem(value, node.rchild, node, 'rchild')

    def insert(self, value):
        """插入一个值"""
        flag, node, parent, nodetype = self.findelem(value, self.root, self.root, None)
        if nodetype == 'lchild':
            parent.lchild = Node(value)
        else:
            parent.rchild = Node(value)

    def preorder(self, node):
        """先序遍历"""
        if node == None:
            return
        print(node.value)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def findmin(self, node):
        """查找最小值"""
        if node.lchild == None:
            return node
        else:
            return self.findmin(node.lchild)

    def delvalue(self, value):
        """删除某个值的节点"""
        flag, node, parent, nodetype = self.findelem(value, self.root, self.root, None)
        if flag == False:
            return
        else:
            if node.lchild != None and node.rchild != None:
                minnode = self.findmin(node.rchild)
                n = minnode.value
                self.delvalue(minnode.value)
                node.value = n
            elif node.lchild == None and node.rchild == None:
                if nodetype == 'lchild':
                    parent.lchild = None
                else:
                    parent.rchild = None
                del node
            else:
                if nodetype == 'lchild':
                    if node.lchild == None:
                        parent.lchild = node.rchild
                    else:
                        parent.lchild = node.lchild
                else:
                    if node.lchild == None:
                        parent.rchild = node.rchild
                    else:
                        parent.rchild = node.lchild
                del node


if __name__ == '__main__':
    b = BinarySearchTree(10)
    b.insert(5)
    b.insert(15)
    b.insert(3)
    b.insert(8)
    b.insert(6)
    b.insert(9)
    b.insert(16)
    b.preorder(b.root)
    flag, *rest = b.findelem(6, b.root, b.root, None)
    print(flag)
    flag, *rest = b.findelem(11, b.root, b.root, None)
    print(flag)
    b.delvalue(5)
    flag, *rest = b.findelem(5, b.root, b.root, None)
    print(flag)
    b.preorder(b.root)
