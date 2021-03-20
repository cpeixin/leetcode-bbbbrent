# coding: utf-8
# Author：Brent
# Date ：2020/6/17 2:49 PM
# Tool ：PyCharm
# Describe ：

import heapq
from heap.heapq_showtree import show_tree


data = [19, 9, 4, 10, 11, 20, 4]

# 创建堆有两种基本方法：heappush()和heapify()。

# heap = []
# print('random :', data)
# print()
# # 当使用heappush()时，当新元素添加时，堆得顺序被保持了。
# for n in data:
#     print('add {:>3}:'.format(n))
#     heapq.heappush(heap, n)
#     show_tree(heap)



# 如果数据已经在内存中，则使用 heapify() 来更有效地重新排列列表中的元素。
# print('random    :', data)
# heapq.heapify(data)
# print('heapified :')
# show_tree(data)




# 正确创建堆后，使用heappop()删除具有最小值的元素。

# print('random    :', data)
# heapq.heapify(data)
# print('heapified :')
# show_tree(data)
# print()
#
# for i in range(2):
#     smallest = heapq.heappop(data)
#     print('pop    {:>3}:'.format(smallest))
#     show_tree(data)


# 在这个例子中，使用 heapify() 和 heappop() 进行排序。
# 要删除现有元素，并在一次操作中用新值替换它们，使用heapreplace()。

# heapq.heapify(data)
# print('start:')
# show_tree(data)
#
# for n in [0, 13]:
#     smallest = heapq.heapreplace(data, n)
#     print('replace {:>2} with {:>2}:'.format(smallest, n))
#     show_tree(data)

# 堆的数据极值 heapq 还包括两个函数来检查 iterable 并找到它包含的最大或最小值的范围。
# 使用nlargest()和nsmallest()仅对 n > 1 的相对较小的值有效，但在少数情况下仍然可以派上用场。
# print('all       :', data)
# print('3 largest :', heapq.nlargest(3, data))
# print('from sort :', list(reversed(sorted(data)[-3:])))
# print('3 smallest:', heapq.nsmallest(3, data))
# print('from sort :', sorted(data)[:3])

#
# 有效地合并排序序列
# 将几个排序的序列组合成一个新序列对于小数据集来说很容易。

# 复制代码对于较大的数据集，将会占用大量内存。不是对整个组合序列进行排序，而是使用 merge() 一次生成一个新序列。
#
# import random
# random.seed(2016)
#
# data = []
# for i in range(4):
#     new_data = list(random.sample(range(1, 101), 5))
#     new_data.sort()
#     data.append(new_data)
#
# for i, d in enumerate(data):
#     print('{}: {}'.format(i, d))
#
# print('\nMerged:')
# for i in heapq.merge(*data):
#     print(i, end=' ')
# print()

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

heap = []
for arr in matrix:
    for index in range(len(arr)):
        heapq.heappush(heap, arr[index])
        show_tree(heap)


