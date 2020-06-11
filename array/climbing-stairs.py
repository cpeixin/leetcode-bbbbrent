def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    method_num = 0
    for i in range(n + 1):
        if i < n:
            if n % (2 * i) == 0:
                method_num += 1
        else:
            if n % 2 * i == 0:
                method_num += 1
    return method_num

if __name__ == '__main__':
    num = climbStairs(100)
    print(num)