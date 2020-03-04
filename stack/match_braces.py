class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"{": "}", "(": ")", "[": "]", "?": "?"}

        stack = ['?']

        for i in s:
            if i in dict:
                stack.append(i)
            else:
                left_char = stack.pop()
                if i != dict[left_char]:
                    return False
        return len(stack) == 1


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')

    lines = '[]()'
    while True:
        try:
            line = '[]()'
            # s = stringToString(line)

            ret = Solution().isValid(line)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
