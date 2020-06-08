import json
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        a_offset = 0
        b_offset = 0

        s = []

        while a_offset < m or b_offset < n:
            if A[a_offset] > B[b_offset]:
                s.append(B[b_offset])
                if (b_offset + 1) >= n:
                    break
                else:
                    b_offset += 1

            else:
                s.append(A[a_offset])
                a_offset += 1
                if (a_offset + 1) >= n:
                    break
                else:
                    a_offset += 1


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            """
            [1,2,3,0,0,0]
            3
            [2,5,6]
            3
            """
            line = next(lines)
            A = stringToIntegerList(line)
            line = next(lines)
            m = int(line)
            line = next(lines)
            B = stringToIntegerList(line)
            line = next(lines)
            n = int(line)

            ret = Solution().merge(A, m, B, n)

            out = integerListToString(A)
            if ret is not None:
                print("Do not return anything, modify A in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
