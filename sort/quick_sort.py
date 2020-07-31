# def quickSort(arr, left=None, right=None):
#     left = 0 if not isinstance(left,(int, float)) else left
#     right = len(arr)-1 if not isinstance(right,(int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quickSort(arr, left, partitionIndex-1)
#         quickSort(arr, partitionIndex+1, right)
#     return arr
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot+1
#     i = index
#     while  i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index+=1
#         i+=1
#     swap(arr,pivot,index-1)
#     return index-1
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]



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
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark



def main():
    array = [8, 2, 4, 7, 10, 1, 7, 12, 6, 7, 16, 18, 19]

    result = quickSort(0, len(array)-1, array)

    print(result)

if __name__ == '__main__':
    main()