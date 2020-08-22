# coding: utf-8
# Author：Brent
# Date ：2020/8/22 10:26 AM
# Tool ：PyCharm
# Describe ：

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 边界条件
        if num1 == '0' or num2 == '0': return '0'

        # 创建结果数组
        ans = [0] * (len(num1) + len(num2))

        # 遍历，按位相乘
        for i in range(len(num1)-1, -1, -1):
            x = int(num1[i])
            for j in range(len(num2)-1, -1, -1):
                ans[i+j+1] += x * int(num2[j])

        # 计算进位
        for i in range(len(ans)-1, 0, -1):
            ans[i-1] += ans[i] // 10
            ans[i]  = ans[i] % 10

        # 遍历ans时的起始index，应该是index 0 还是 index 1
        index = 1 if ans[0] == 0 else 0

        # 生成结果
        res = ''.join(str(num) for num in ans[index:])

        return res



if __name__ == '__main__':
    solution = Solution()
    num1 = "123"
    num2 = "456"
    res = solution.multiply(num1, num2)
    print(res)
