import time

"""
第一个(外层)for循环作用：控制排序的轮数
第二个(内层)for循环作用：控制每一轮里的每一个比较步骤

"""
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def bubble_sort_v2(arr):
    """改进版，避免右侧最大值重复比较"""
    for i in range(len(arr) - 1, 0, -1):  # 反向遍历
        for j in range(0, i):  # 由于最右侧的值已经有序，不再比较，每次都减少遍历次数
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    array = [3,4,1,2,5,6]
    result_array = bubble_sort(array)
    array.sort()
    print(result_array)




if __name__ == '__main__':
    main()