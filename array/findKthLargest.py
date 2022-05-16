
'''
Author: your name
Date: 2022-03-14 17:02:34
LastEditTime: 2022-03-14 17:02:35
LastEditors: Please set LastEditors
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

快排~~
注意：随机化切分元素。快速排序虽然快，但是在遇到特殊测试用例（顺序数组或者逆序数组）的时候，递归树会退化成链表，时间复杂度会变成 O(N^2)

我们在学习「快速排序」的时候，会学到 partition（切分），通过 partition 操作使得：对于某个下标 j，nums[j] 已经排定，
即 nums[j] 经过 partition（切分）操作以后会放置在它「最终应该放置的地方」。

而且：
nums[left] 到 nums[j - 1] 中的所有元素都不大于 nums[j]；
nums[j + 1] 到 nums[right] 中的所有元素都不小于 nums[j]。

利用快速排序的思想，从数组 S 中随机找出一个元素 X，把数组分为两部分 Sa 和 Sb。Sa 中的元素大于等于 X，Sb 中元素小于 X。这时有两种情况：

Sa 中元素的个数小于 k，则 Sb 中的第 k-|Sa| 个元素即为第k大数；
Sa 中元素的个数大于等于 k，则返回 Sa 中的第 k 大数。时间复杂度近似为 O(n)

'''


class Solution:
    # 采用快速排序方法，分成的数列左边大于右边
    def findKthLargest(self, nums, k):
        n = len(nums)
        if (k > n):
            return
        index = self.quickSort(nums, 0, n - 1, k)
        return nums[index]

    def quickSort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return self.quickSort(nums, l, p - 1, k)
        else:
            return self.quickSort(nums, p + 1, r, k)

    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = solution.findKthLargest(nums, k)
    print(result)