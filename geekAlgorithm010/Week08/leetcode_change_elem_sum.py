"""超出时间限制"""
def findSwapValues(array1 , array2):
    array1_sum = sum(array1)
    array2_sum = sum(array2)

    result_list = []

    for i in array1:
        for j in array2:
            if array1_sum - i + j == array2_sum - j + i:
                result_list.append([i, j])

    if result_list:
        return result_list[0]
    return result_list


def findSwapValues_m1(array1, array2):
    diff = sum(array1) - sum(array2)
    if diff & 1: return []
    """ >> 右移， >>= 1右移1位 相当于除以二"""
    diff >>= 1
    s2 = set(array2)
    for a in array1:
        if a - diff in s2:
            return [a, a - diff]
    return []



def main():
    array1 = [4, 1, 2, 1, 1, 2]
    array2 = [3, 6, 3, 3]
    result = findSwapValues_m1(array1, array2)

    print(result)


if __name__ == '__main__':
    main()