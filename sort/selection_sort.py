def selection_sort(array):
    for i in range(0, len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]

    print(array)




def main():
    array = [3,4,1,7,2,6,5]
    selection_sort(array)


if __name__ == '__main__':
    main()