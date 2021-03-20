布隆过滤器BloomFilter<br />应用场景：判断一个元素时候存在于一个集合中，效率远远高于其他数据结构实现<br />python实现
```python
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
```


<a name="MRwOA"></a>
#### [LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)
有序字典实现
```python
import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.OrderedDict()
        self.size = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.size > 0:
                self.size -= 1
            else:
                self.cache.popitem(last = False)
        self.cache[key] = value


```

<br />HashTable + 双向链表实现
```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        # 哨兵节点  避免判断节点前后是否有节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1
        
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else: # key不在cache中
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                tail_node = self.remove_tail()
                self.cache.pop(tail_node.key)
                self.size -= 1
                
                
    def add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        
    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)
        
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def remove_tail(self):
        node = self.tail.pre
        self.remove(node)
        return node
       
```
复杂度分析<br />
<br />时间复杂度：对于 put 和 get 都是 O(1)。<br />
<br />空间复杂度：O(capacity)，因为哈希表和双向链表最多存储 capacity+1 个元素。<br />![截屏2020-07-28 上午12.33.40.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596034134968-00c03f6c-bdbe-45ca-a3d1-5f87f75a5175.png#align=left&display=inline&height=702&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-28%20%E4%B8%8A%E5%8D%8812.33.40.png&originHeight=702&originWidth=1462&size=502760&status=done&style=none&width=1462)![截屏2020-07-28 上午12.34.31.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596034135999-54e393e4-434b-44a0-bf0b-1f6fb9f6f7b5.png#align=left&display=inline&height=758&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-28%20%E4%B8%8A%E5%8D%8812.34.31.png&originHeight=758&originWidth=1064&size=299156&status=done&style=none&width=1064)![截屏2020-07-28 上午12.36.49.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596034137026-7de36dde-1411-4fb6-9978-bab89437d008.png#align=left&display=inline&height=774&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-28%20%E4%B8%8A%E5%8D%8812.36.49.png&originHeight=774&originWidth=1326&size=373256&status=done&style=none&width=1326)![截屏2020-07-28 上午12.39.26.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596034138518-0cb6f305-232b-4322-8d69-b08807ab4d1f.png#align=left&display=inline&height=676&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-28%20%E4%B8%8A%E5%8D%8812.39.26.png&originHeight=676&originWidth=1412&size=515551&status=done&style=none&width=1412)![截屏2020-07-28 上午1.09.49.png](https://cdn.nlark.com/yuque/0/2020/png/1072113/1596034133912-d25c45cc-d43e-4725-80ce-f43d26971d2b.png#align=left&display=inline&height=634&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2020-07-28%20%E4%B8%8A%E5%8D%881.09.49.png&originHeight=634&originWidth=1434&size=354204&status=done&style=none&width=1434)<br />
<br />冒泡排序：<br />它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端<br />![849589-20171015223238449-2146169197.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1596164408232-bd473dc5-fd04-4134-b8b7-0c5cbb8bb721.gif#align=left&display=inline&height=257&margin=%5Bobject%20Object%5D&name=849589-20171015223238449-2146169197.gif&originHeight=257&originWidth=826&size=466890&status=done&style=none&width=826)
```python
for i in range(0, len(array)-1):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
return array
```

<br />选择排序：<br />工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。<br />**n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果**<br />**![849589-20171015224719590-1433219824.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1596164427680-b74935a5-6d71-4176-8d80-f76818487ae3.gif#align=left&display=inline&height=248&margin=%5Bobject%20Object%5D&name=849589-20171015224719590-1433219824.gif&originHeight=248&originWidth=811&size=628926&status=done&style=none&width=811)**
```python
for i in range(0, len(array) - 1):
    min_index = i
    # 一轮比较，找出未排序序列中，最小的元素
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    if i != min_index:
        array[i], array[min_index] = array[min_index], array[i]
return array
```
表现最稳定的排序算法之一，因为无论什么数据进去都是O(n)的时间复杂度，所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。理论上讲，选择排序可能也是平时排序一般人想到的最多的排序方法了吧。<br />
<br />插入排序：<br />它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

- 从第一个元素开始，该元素可以认为已经被排序；
- 取出下一个元素，在已经排序的元素序列中从后向前扫描；
- 如果该元素（已排序）大于新元素，将该元素移到下一位置；

![849589-20171015225645277-1151100000.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1596164462342-dc3ee0e3-a094-469e-933c-e089a9d1c9d4.gif#align=left&display=inline&height=505&margin=%5Bobject%20Object%5D&name=849589-20171015225645277-1151100000.gif&originHeight=505&originWidth=811&size=404492&status=done&style=none&width=811)
```python
for i in range(1, len(array)):
    preIndex = i-1
    curr = array[i]
    while preIndex >=0 and array[preInedx] > curr:
        array[preInedx+1] = array[preInedx]
        preInedx -= 1
    array[preInedx+1] = curr
return array
```
插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。<br />
<br />
<br />归并排序：<br />归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 <br />![849589-20171015230557043-37375010.gif](https://cdn.nlark.com/yuque/0/2020/gif/1072113/1596168131075-cfcb3a6f-126b-4f6c-bad0-618d4be55e44.gif#align=left&display=inline&height=505&margin=%5Bobject%20Object%5D&name=849589-20171015230557043-37375010.gif&originHeight=505&originWidth=811&size=376572&status=done&style=none&width=811)
```python
 def merge(a_list, b_list):
    # 所要利用的额外空间
    result = []
    a_index, b_index = 0, 0
    # index从0开始，所以 < 号
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            result.append(a_list[a_index])
            a_index += 1
        else:
            result.append(b_list[b_index])
            b_index += 1
    if a_index == len(a_list):
        for i in b_list[b_index:]:
            result.append(i)
    else:
        for i in a_list[a_index:]:
            result.append(i)
    return result

def mergeSort(total_list):
    if len(total_list) <= 1:
        return total_list
    mid = len(total_list) >> 1
    left = mergeSort(total_list[:mid])
    right = mergeSort(total_list[mid:])
    return merge(left, right)
```
归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。<br />
<br />快速排序：<br />快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
```python
def quickSort(array, begin, end):
    if begin > end: return 
    pivot = partition(array, begin, end)
    quickSort(array, begin, pivot - 1)
    quickSort(array, pivot + 1, end)
    return array
    
def partition(array, begin, end):
    # 默认指定pivot为begin,counter为比pivot小数值计数
    pivot = array[begin]
    counter = begin
    for i in range(begin+1, end+1):
        if array[i] < pivot:
            counter+=1
            array[counter], array[i] = array[i], array[counter]
    array[counter], array[begin] = array[begin], array[counter]
    return counter
```

<br />

<a name="soBOX"></a>
### 题解


<a name="dHM2r"></a>
#### [合并区间](https://leetcode-cn.com/problems/merge-intervals/)
题解：<br />给出一个区间的集合，请合并所有重叠的区间。<br />示例 1:<br />输入: [[1,3],[2,6],[8,10],[15,18]]<br />输出: [[1,6],[8,10],[15,18]]<br />
<br />代码：
```python
class Solution:
    def merge(self, intervals):
        if not intervals: return []
        #  对整个序列中的子序列进行升序排序
        intervals.sort(key = lambda x: x[0])
        # 定义结果集
        result = []
        for interval in intervals:
            # 结果集为空则直接添加
            # 结果集最后一个子集的右边界如果小于目前子集的左边界，则无重合
            # eg. (1,2) (3,6) 
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                #有重合的情况下要判断两个子集的右边界的最大值，对result子集进行更新
                result[-1][1] = max(interval[1], result[-1][1])
        return result
```

<br />复杂度分析：<br />时间复杂度：O(nlogn)，其中 n 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlogn)。<br />
<br />空间复杂度：O(logn)，其中 n 为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(logn) 即为排序所需要的空间复杂度。<br />
<br />

<a name="fhNuB"></a>
#### [数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)
题解：<br />给你两个数组，arr1 和 arr2，<br />arr2 中的元素各不相同<br />arr2 中的每个元素都出现在 arr1 中<br />对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。<br />
<br />代码：
```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        num_dict = collections.defaultdict(int)
        not_in_arr2 = []
        result = []
        # 将arr1中元素全部计数到Hash表中
        for num in arr1:
            # 将arr2中没有的元素挑出，并且考虑重复的问题
            if num not in arr2 and num not in not_in_arr2:
                not_in_arr2.append(num)
            num_dict[num] += 1

        # 先遍历arr2，按照Hash表中的value数，拼接结果
        for num in arr2:
            value = num_dict[num]
            result += [num] * value

        # 对arr2中没有出现的元素升序排序
        not_in_arr2.sort()

        # 最后对未出现的元素拼接
        for num in not_in_arr2:
            value = num_dict[num]
            result += [num] * value
        return result

```

<br />复杂度分析：<br />时间复杂度：O(arr1.length + not_in_arr2.length*log(not_in_arr2.length))<br />空间复杂度：O(arr1.length)<br />
<br />

<a name="jtn58"></a>
#### [翻转对](https://leetcode-cn.com/problems/reverse-pairs/)
题解：<br />给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。<br />你需要返回给定数组中的重要翻转对的数量。<br />示例 1:<br />输入: [1,3,2,3,1]<br />输出: 2<br />
<br />代码：<br />
<br />**复杂度分析**

- 时间复杂度：_O_(_N_log_N_)。<br />
- 空间复杂度：O(N)。


<br />
<br />
<br />

