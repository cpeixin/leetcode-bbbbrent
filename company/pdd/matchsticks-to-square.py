# coding: utf-8
# Author：Brent
# Date ：2020/9/14 2:48 PM
# Tool ：PyCharm
# Describe ：


class Solution:
    def makesquare(self, nums):
        if not nums: return False
        sum_length = sum(nums)
        possible_side = sum_length // 4
        nums_size = len(nums)

        if possible_side * 4 != sum_length: return False

        side = [0 for _ in range(4)]
        nums.sort(reverse=True)
        def dfs(index):
            if index == nums_size:
                return side[0] == side[1] == side[2]== side[3] == possible_side
            for i in range(4):
                if side[i] + nums[index] <= possible_side:
                    side[i] += nums[index]
                    if dfs(index+1): return True
                    side[i] -= nums[index]
            return False
        return dfs(0)


if __name__ == '__main__':
    nums = [1,1,2,2,2]
    solution = Solution()
    solution.makesquare(nums)