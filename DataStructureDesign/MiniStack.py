# coding: utf-8
# Author：Brent
# Date ：2020/8/21 10:52 PM
# Tool ：PyCharm
# Describe ：

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini_stack = []


    def pop(self):
        remove_value = self.stack.pop()
        if self.mini_stack and remove_value == self.mini_stack[-1]:
            self.mini_stack.pop()



    def push(self, value):
        self.stack.append(value)
        if not self.mini_stack or value <= self.mini_stack[-1]:
            self.mini_stack.append(value)


    def top(self):
        return self.stack[-1]


    def getMin(self):
        return self.mini_stack[-1]