nums = [2, 2, 11, 15]


def twoSum(nums, target):
    # hashmap={}
    # for ind,num in enumerate(nums):
    #     hashmap[num] = ind
    # for i,num in enumerate(nums):
    #     j = hashmap.get(target - num)
    #     if j is not None and i!=j:
    #         return [i,j]

    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i


if __name__ == '__main__':
    twoSum(nums, 9)
    a = dict()
