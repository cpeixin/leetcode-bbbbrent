def subSort(array):
    sorted_list = sorted(array)

    for i in range(len(array)):
        if array[i] != sorted_list[i]:
            start = i
            break

    for j in range(len(array)):
        j = len(array) - 1 - j
        if array[j] != sorted_list[j]:
            end = j
            break

    print([start, end])


def main():
    array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    subSort(array)



if __name__ == '__main__':
    main()