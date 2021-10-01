#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 9:44 上午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : CQueue.py
# @Description:

class CQueue:
    def __init__(self):
        self.appendTailStack = []
        self.deleteHeadStack = []

    def appendTail(self, value):
        self.appendTailStack.append(value)

    def deleteHead(self):
        if self.deleteHeadStack:
            return self.deleteHeadStack.pop()
        if not self.appendTailStack:
            return -1
        while self.appendTailStack:
            self.deleteHeadStack.append(self.appendTailStack.pop())
        return self.deleteHeadStack.pop()
