class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums)
        # 我们首先将所有元素反转。然后反转前 k 个元素，再反转后面 n-k 个元素
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)


    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1