# coding: utf-8
# Author：Brent
# Date ：2020/7/31 9:29 PM
# Tool ：PyCharm
# Describe ：布隆过滤器 Python 代码示例

from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self,size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.serall(0)


    def add(self, data):
        for seed in range(self.hash_num):
            result = mmh3.hash(seed, data)
            self.bit_array[result] = 1


    def lookup(self, data):
        for seed in range(self.hash_num):
            result = mmh3.hash(seed, data)
            if self.bit_array[result] == 0: return 'No this data'

        return 'Probably'

if __name__ == '__main__':
    bf = BloomFilter(500000, 7)
    bf.add("dantezhao")
    print(bf.lookup("dantezhao"))
    print(bf.lookup("yyj"))
