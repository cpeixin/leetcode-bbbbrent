def quickSort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quickSort(begin, pivot_index - 1, nums)
    quickSort(pivot_index + 1, end, nums)
    return nums


def partition(begin, end, nums):
    pivot = nums[begin]
    # 小于pivot元素的个数
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            # 这里的逻辑和移动零一样
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    # 和最后一个比他小的换位置
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark


def main():
    array = [4, 3, 1, 6, 7, 2, 9]
    result = quickSort(0, len(array) - 1, array)
    print(result)


if __name__ == '__main__':
    main()
