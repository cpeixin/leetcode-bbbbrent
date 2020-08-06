# coding: utf-8
# Author：Brent
# Date ：2020/8/5 11:45 AM
# Tool ：PyCharm
# Describe ：
class Solution:
    def changeNums(self, nums):
        _count, count = 0, 0
        for num in nums:
            if num > 0: count += 1
            else: _count += 1

        slow, fast = 0, 1
        if abs(count - _count) == 1:
            # 正数开头
            if count > _count:
                while fast < len(nums):
                    if nums[fast] * nums[slow] > 0 and nums[slow] > 0:
                        fast += 1
                    else:
                        slow += 1
                        nums[fast], nums[slow] = nums[slow], nums[fast]
                        fast = slow + 1
                return nums
            else: # 负数开头
                while fast < len(nums):
                    if nums[fast] * nums[slow] > 0 and nums[slow] < 0:
                        fast += 1
                    else:
                        slow += 1
                        nums[fast], nums[slow] = nums[slow], nums[fast]
                        fast = slow + 1
                return nums

        else:
            return nums



if __name__ == '__main__':
    nums = [1, 2, -1, -2, -3]
    solution = Solution()
    print(solution.changeNums(nums))