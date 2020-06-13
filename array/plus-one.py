# coding: utf-8
# Author：Brent
# Date ：2020/6/13 6:36 PM
# Tool ：PyCharm
# Describe ：


def plusOne(digits):
    length = len(digits) - 1

    while digits[length] == 9:
        digits[length] = 0
        length -= 1
    if (length < 0):
        digits = [1] + digits
    else:
        digits[length] += 1
    return digits


if __name__ == '__main__':
    digits = [9,9,9,9]
    result = plusOne(digits)
    print(result)