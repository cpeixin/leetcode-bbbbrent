import collections


# 双端队列
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    deque = collections.deque()
    res = []
    for i, num in enumerate(nums):
        # deque[0]左端第一个元素， i-k ，当前窗口的左边界
        while deque and deque[0] <= i - k:
            deque.popleft()  # outdata indices 移出不属于当前窗口的元素
        while deque and num > nums[deque[-1]]:  # deque[-1]右端最后一个元素，比较当前num是否比队列头元素大。
            deque.pop()  # 队尾出一个元素
        deque.append(i)  # append 队尾添加元素
        # 大于等于第一个窗口右边界时，则在队列头部添加最大元素
        if i >= k - 1:
            # 队列中最大的元素肯定是在头部，也就是左端。
            # 因为在这步，while deque and num > nums[deque[-1]] 已经将小于当前窗口新近元素的元素都pop()了出去
            res.append(nums[deque[0]])
    return res


# 堆
import heapq

def maxSlidingWindow_heap(nums, k):
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # how to get max value among the window
    # use maximum heap (-value, index)

    # Time complexity : O(NlogN)
    # Space complexity: O(N)

    res, heap = [], []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i + 1 >= k:
            while heap and heap[0][1] < i + 1 - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
    return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7, 1, 2, 3, 4]
    k = 3
    result = maxSlidingWindow_heap(nums, k)
    print(result)
    # d = collections.deque()
    # d.append(1)
    # d.append(2)
    # d.appendleft(3)
    # print(d)
    # print(d[0])
    # print(d[-1])
    # d.pop()
    # print(d)
