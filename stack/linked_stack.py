from typing import Optional


class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next


class linkstack:
    def __init__(self):
        self.top: Node = None

    def push(self, value: int):
        new_node = Node(value)
        new_node.next = self.top

        self.top = new_node

    def pop(self)->Optional[int]:
        if self.top:
            data = self.top.data
            self.top = self.top.next

            return data

    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join(f"{num}]" for num in nums)


if __name__ == "__main__":
    stack = linkstack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
