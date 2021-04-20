# coding: utf-8
# Author：Brent
# Date ：2020/6/22 10:40 PM
# Tool ：PyCharm
# Describe ：设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。

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
