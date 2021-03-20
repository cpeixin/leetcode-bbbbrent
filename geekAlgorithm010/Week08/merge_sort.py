def Merge(a, p, q, r):
    leftArray = []
    rightArray = []
    n1 = q - p + 1 + 1
    n2 = r - q + 1
    for num in range(1, n1):
        index = num + p - 1
        leftArray.append(a[index])
    leftArray.append(float("inf"))
    for num in range(1, n2):
        index = num + q
        rightArray.append(a[index])
    rightArray.append(float("inf"))
    i = 0
    j = 0
    print(leftArray)

    print(rightArray)

    for k in range(p, r + 1):
        if (leftArray[i] <= rightArray[j]):
            a[k] = leftArray[i]
            i = i + 1
        else:
            a[k] = rightArray[j]
            j = j + 1
    print(a)



def Merge_Sort(a, p, r):
    if (p < r):
        q = int((p + r) / 2)
        Merge_Sort(a, p, q)  # 排序数组的半部分
        Merge_Sort(a, q + 1, r)  # 排序数组的后半部分
        Merge(a, p, q, r)  # 将两个排序好的数组


if __name__ == '__main__':

    a = [2, 4, 9, 8, 1, 3, 5, 7]
    Merge_Sort(a, 0, 7)
