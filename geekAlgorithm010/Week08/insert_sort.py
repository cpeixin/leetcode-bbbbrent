def insert_sort_1(arr):
    for i in range(1, len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    print(arr)


def main():
    array = [3,4,1,2,7,5,6]
    insert_sort_1(array)


if __name__ == '__main__':
    main()