def binarySearch_first(array, array_size, search_value):
    """查找第一个值等于给定值的元素"""
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] == search_value:
            while array[mid-1] == search_value:
                if mid - 1 == 0:
                    return 0
                mid -= 1
            return mid
        elif array[mid] < search_value:
            low = mid + 1
        else:
            high = mid - 1


def binarySearch_first_better(array, array_size, search_value):
    """查找第一个值等于给定值的元素"""
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] < search_value:
            low = mid + 1
        elif array[mid] > search_value:
            high = mid - 1
        else:
            if mid == 0 or array[mid - 1] != search_value:
                return mid
            high = mid - 1


def binarySearch_last(array, array_size, search_value):
    """查找第一个值等于给定值的元素"""
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] < search_value:
            low = mid + 1
        elif array[mid] > search_value:
            high = mid - 1
        else:
            if mid == array_size-1 or array[mid + 1] != search_value:
                return mid
            low = mid + 1

def binarySearch_firstbig(array, array_size, search_value):
    """查找第一个大于等于给定值的元素"""
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] >= search_value:
            if mid == 0 or array[mid - 1] < search_value:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1

def binarySearch_lastsmall(array, array_size, search_value):
    """查找最后一个小于等于给定值的元素"""
    low = 0
    high = array_size - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        if array[mid] < search_value:
            low = mid + 1
        elif array[mid] > search_value:
            high = mid - 1
        else:
            if mid == 0 or array[mid - 1] != search_value:
                return mid-1
            high = mid - 1




def main():
    array = [1, 1, 24, 35, 36, 48, 53, 56, 56, 56, 60, 61, 62, 63, 63, 70, 89]
    offset = binarySearch_firstbig(array, len(array), 56)
    print(offset)

if __name__ == '__main__':
    main()


"""
0 1
1 2
2 24
3 35
4 36
5 48
6 53
7 56
8 56
9 56
10 60
11 61
12 62
13 63
14 63
15 70
16 89
"""