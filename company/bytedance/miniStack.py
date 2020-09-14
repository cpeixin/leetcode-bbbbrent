# coding: utf-8
# Author：Brent
# Date ：2020/8/21 10:08 PM
# Tool ：PyCharm
# Describe ：设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。


class MiniStack:
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


if __name__ == '__main__':
    mini_stack = MiniStack()
    mini_stack.push(5)
    mini_stack.push(4)
    mini_stack.push(3)
    mini_stack.push(2)
    mini_stack.push(1)

    mini_stack.pop()
    mini_stack.top()
    mini_stack.getMin()
