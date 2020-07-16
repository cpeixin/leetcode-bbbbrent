# coding: utf-8
# Author：Brent
# Date ：2020/7/8 11:22 PM
# Tool ：PyCharm
# Describe ：你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。
#
# 示例：
#
# 输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： {3,4,5,6}
# 提示：
#
# 0 < shorter <= longer
# 0 <= k <= 100000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diving-board-lcci

class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        # 本题有两个特例
        if k == 0: return {}
        if shorter == longer: return {longer * k}

        return {longer*step+shorter*(k-step) for step in range(k+1)}

if __name__ == '__main__':
    solution = Solution()
    print(solution.divingBoard(1,2, 3))