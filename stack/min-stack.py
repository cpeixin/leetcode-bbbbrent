# coding: utf-8
# Author：Brent
# Date ：2020/6/22 10:40 PM
# Tool ：PyCharm
# Describe ：

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, x):
        self.stack.append(x)
        # 这里注意： x <= self.min_stack[-1]    <=
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(-1)
    min_stack.push(4)
    min_stack.push(7)

    min_stack.pop()
    min_stack.pop()
    min_stack.pop()

    min_stack.top()
