from typing import List


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         last_char = s.pop()
#         print(last_char)
#         if len(s) != 0:
#             return self.reverseString(s)

class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """

        def helper(start, end, ls):
            if start >= end:
                return

            # swap the first and last element
            ls[start], ls[end] = ls[end], ls[start]

            return helper(start + 1, end - 1, ls)

        helper(0, len(s) - 1, s)


if __name__ == '__main__':
    list = ["h", "e", "l", "l", "o"]
    solution = Solution()

    solution.reverseString(list)
