from typing import List


class Solution:
    def minNumber(self, nums: List[int]):
        for i in range(len(nums)):
            flag = False
            for j in range(len(nums) - i - 1):
                if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                    self.swap(nums, j, j + 1)
                    flag = True
            if flag: break

        strs = [str(num) for num in nums]
        print(''.join(strs))

    def swap(self, nums: List[int], a: int, b: int):
        nums[a] = nums[a] ^ nums[b]
        nums[b] = nums[b] ^ nums[a]
        nums[a] = nums[a] ^ nums[b]


if __name__ == '__main__':
    arr = [10, 2]
    solution = Solution()
    solution.minNumber(arr)
