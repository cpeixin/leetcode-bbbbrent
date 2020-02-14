class stack:
    def __init__(self, size):
        """
        栈结构
        :param size: 栈大小
        """
        self.count = 0
        self.size = size
        self.array = []

    def push(self, value):
        """
        入栈  入栈判满
        :param value:
        """
        if self.count == self.size:
            return False
        self.array.append(value)
        self.count += 1
        return True

    def pop(self):
        """
        出栈  出栈判空
        :return:
        """
        if self.count == 0:
            return False
        data = self.array[self.count - 1]
        self.count -= 1

        return data


if __name__ == '__main__':
    st = stack(4)

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.pop()
    st.pop()
    st.pop()
    data = st.pop()

    print(data)

    st.pop()