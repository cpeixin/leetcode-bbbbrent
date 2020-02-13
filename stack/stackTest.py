if __name__ == '__main__':
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(stack.pop())
    print(stack.pop())

    dict = {'{': '}', '(': ')', '[': ']', '?': '?'}

    if '}' in dict:
        print('存在')
    else:
        print('不存在')
