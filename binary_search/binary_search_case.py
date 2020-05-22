def binarySearch(array, array_size, search_value):
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] == search_value:
            return mid
        elif mid < search_value:
            low = mid + 1
        else:
            high = mid - 1


def main():
    array = []
    for i in range(100):
        array.append(i)

    mid_num = binarySearch(array, len(array), 57)
    print(mid_num)


if __name__ == '__main__':
    main()
