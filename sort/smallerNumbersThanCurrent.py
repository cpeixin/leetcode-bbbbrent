# coding: utf-8
# Author：Brent
# Date ：2020/10/26 11:46 PM
# Tool ：PyCharm
# Describe ：给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
#
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
#
# 以数组形式返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        place = [0] * 101
        output = []

        for n in nums:
            place[n] += 1  # 把从0 - 100的所有数的个数都数出来了。

        lessthan = []  # 把从0 - 100的所有数的比它小的数的个数都列出来。
        temp = 0  # 其实就是刚才的place数组的累加
        for p in place:
            lessthan.append(temp)
            temp += p

        for n in nums:  # 最后对应nums把lessthan的值掏出来作为输出。
            output.append(lessthan[n])

        return output


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    res = Solution().smallerNumbersThanCurrent(nums)
    print(res)
