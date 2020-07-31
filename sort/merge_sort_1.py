def merge(a_list, b_list):
    # 所要利用的额外空间
    result = []
    a_index, b_index = 0, 0
    # index从0开始，所以 < 号
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            result.append(a_list[a_index])
            a_index += 1
        else:
            result.append(b_list[b_index])
            b_index += 1
    if a_index == len(a_list):
        for i in b_list[b_index:]:
            result.append(i)
    else:
        for i in a_list[a_index:]:
            result.append(i)
    return result


def mergeSort(total_list):
    if len(total_list) <= 1:
        return total_list
    mid = len(total_list) >> 1
    left = mergeSort(total_list[:mid])
    right = mergeSort(total_list[mid:])
    return merge(left, right)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(mergeSort(a))
