def bucket_sort(lst):
    """创建桶"""
    buckets = [0] * ((max(lst) - min(lst))+1)
    for i in range(len(lst)):
        """对应下标添加标识位"""
        buckets[lst[i]-min(lst)] += 1
    res=[]
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    print(res)


def main():
    array = [5,3,6,2,7,5,10,11,20]
    array.sort()
    bucket_sort(array)


if __name__ == '__main__':
    main()