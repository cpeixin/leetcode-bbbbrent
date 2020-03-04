class LNode():
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class StackUnderflow(ValueError):  # 栈下溢，空栈访问
    pass


class LStack():  # 基于链接表技术实现的栈类，用LNode作为结点
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem


class Solution(object):
    """  """
    def removeOuterParentheses(self, S):
    #
    #     count = 0
    #     result = ''
    #     for i in S:
    #         if i == '(':
    #
    #             count += 1
    #             if count > 1:
    #                 result += i
    #         else:
    #             if count > 1:
    #                 result += i
    #
    #             count -= 1
    #     return result
        stack = []
        result = ""

        for each in S:
            if each == "(":
                if stack:  # 如果栈是空的话
                    result += each  # 表示当前"("是最外层括号
                stack.append(each)  # 添加当前的"("到栈中
            else:
                stack.pop()  # 把与"("匹配的括号从队列中弹出
                if stack:  # 如果"("不是队列中的最后一个, 加到result中
                    result += each

        return result


if __name__ == '__main__':
    str = '(()())'
    s = Solution()
    result = s.removeOuterParentheses(str)
    print(result)


