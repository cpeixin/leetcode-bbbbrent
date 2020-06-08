class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        upper = self.generate(numRows - 1)
        upper.append([1] + [upper[-1][i - 1] + upper[-1][i] for i in range(1, numRows - 1)] + [1])
        return upper

    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        else:
            res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            res.append([1] + [res[i - 1][j] + res[i - 1][j + 1] for j in range(i - 1)] + [1])
        return res[rowIndex][:]




if __name__ == '__main__':
    solution = Solution()
    result = solution.getRow_2(4)
    print(result)
