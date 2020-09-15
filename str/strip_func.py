# coding: utf-8
# Author：Brent
# Date ：2020/9/15 2:38 PM
# Tool ：PyCharm
# Describe ：' a b c ' -> 'a b c'




class Solution:
   def strip_functions(self,str):
       if not str: return ''
       str_len = len(str)

       left_index = 0
       right_index = str_len - 1


       while str[left_index] == ' ':
           left_index += 1

       while str[right_index] == ' ':
           right_index -= 1

       str.strip()

       return str[left_index:right_index+1]





if __name__ == '__main__':
    s = '      '
    solution = Solution()
    print(solution.strip_functions(s))