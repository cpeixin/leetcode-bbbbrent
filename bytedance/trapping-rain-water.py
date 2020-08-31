# coding: utf-8
# Author：Brent
# Date ：2020/8/31 11:03 PM
# Tool ：PyCharm
# Describe ：给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        max_rain = 0
        max_left = 0
        max_right = height[len(height)-1]

        left_index, right_index = 0, len(height)-1
        while left_index < right_index:
            if height[left_index] < height[right_index]:
                if max_left > height[left_index]:
                    max_rain += (max_left - height[left_index])
                max_left = max(max_left, height[left_index])
                left_index += 1
            else:
                if max_right > height[right_index]:
                    max_rain += (max_right - height[right_index])
                max_right = max(max_right, height[right_index])
                right_index -= 1
        return max_rain


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    res = solution.trap(height)
    print(res)
