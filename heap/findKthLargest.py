'''
Author: your name
Date: 2021-07-02 13:17:05
LastEditTime: 2021-07-02 13:17:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-bbbbrent/heap/findKthLargest.py
'''

class findKthLargest:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def adju_max_heap(nums_list, in_node):  # 从当前内部节点处修正大根堆
            """"in_node是内部节点的索引"""
            l, r, large_idx= 2*in_node+1, 2*in_node+2, in_node  # 最大值的索引默认为该内部节点

            if l < len(nums_list) and nums_list[large_idx] < nums[l]:  
                # 如果左孩子值大于该内部节点的值，则最大值索引指向左孩子
                large_idx = l
            if r < len(nums_list) and nums_list[large_idx] < nums[r]:
                # 如果执行了上一个if语句，此时最大值索引指向左孩子，否则还是指向该内部节点
                # 然后最大值索引指向的值和右孩子的值比较
                large_idx = r

            # 上述两个if就是得到(内部节点，左孩子，右孩子)中最大值的索引
            if large_idx != in_node: # 如果最大值在左孩子和右孩子中，则和内部节点交换
                nums_list[large_idx], nums_list[in_node] = nums_list[in_node], nums_list[large_idx]
                # 如何内部节点是和左孩子交换，那就递归修正它的左子树，否则递归修正它的右子树
                adju_max_heap(nums_list, large_idx)

        def build_max_heap(nums_list):  # 由列表建立大根堆
            """"从后往前遍历所有内部节点，其中最后一个内部节点的公式为len(nums_list)//2 - 1"""
            for in_node in range(len(nums_list)//2 - 1, -1, -1):
                adju_max_heap(nums_list, in_node)
        
        def find_kth_max(nums_list, k):  # 从列表中找到第k个最大的
            build_max_heap(nums_list)  # 先建立大根堆
            for _ in range(k-1):
                nums_list[0], nums_list[-1] = nums_list[-1], nums_list[0]  # 堆头和堆尾交换
                nums_list.pop()  # 删除堆尾
                adju_max_heap(nums_list, 0)  # 从堆头处开始修正大根堆
            return nums_list[0]
        return find_kth_max(nums, k) 