# coding: utf-8
# Author：Brent
# Date ：2020/6/30 10:43 PM
# Tool ：PyCharm
# Describe ：还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
#
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
#
# 示例 1:
#
# 输入: [1,1,2,2,2]
# 输出: true
#
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例 2:
#
# 输入: [3,3,3,3,4]
# 输出: false
#
# 解释: 不能用所有火柴拼成一个正方形。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/matchsticks-to-square

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        # 可以理解成目前数组可以构成的正方形周长
        square_length = sum(nums)
        # 数组的长度
        nums_size = len(nums)
        # 可能的正方形边长, //整除得到的最大整数
        possible_side = square_length // 4
        # 判断是否与上面计算的周长相等
        if possible_side*4 != square_length: return False
        # 构建存储四条边结构
        sides = [0 for _ in range(4)]
        # 对数组进行排序，降序排列有利于计算，类似于剪枝
        nums.sort(reverse=True)
        # 定义递归回溯函数
        def backtrack(index):
            # 长度全部遍历完，如果四条边相等，则可以构成正方形
            if index == nums_size:
                return sides[0] == sides[1] == sides[2] == possible_side
            for i in range(4):
                # 如果当前i边满足了possible_side可能边大小长度，则遍历下一个边
                if sides[i]+nums[index] <= possible_side:
                    sides[i]+=nums[index]
                    if backtrack(index+1): return True
                    # 不可缺少的一步，回撤
                    sides[i]-=nums[index]
            return False
        #实例化的同时，判断返回结果
        return backtrack(0)


if __name__ == '__main__':
    nums = [5,5,5,5,4,4,4,4,3,3,3,3]
    solution = Solution()
    result = solution.makesquare(nums)
    print(result)