import collections


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
        while deque and num > nums[deque[-1]]:# deque[-1]右端最后一个元素，比较当前num是否比队列头元素大。
            deque.pop() # 队尾出一个元素
        deque.append(i) # append 队尾添加元素
        # 大于等于第一个窗口右边界时，则在队列头部添加最大元素
        if i >= k - 1:
            # 队列中最大的元素肯定是在头部，也就是左端。
            # 因为在这步，while deque and num > nums[deque[-1]] 已经将小于当前窗口新近元素的元素都pop()了出去
            res.append(nums[deque[0]])
    return res

    # q, res = [], []
    # for i in range(len(nums)):
    #     if not q:  # 如果为空直接加入队列
    #         q.append(i)
    #     else:
    #         if i == q[0] + k:  # 如果队首的索引已位于滑动窗口之外，将其出队
    #             q.pop(0)
    #         while q and nums[q[-1]] < nums[i]:  # 将小于当前值的队尾元素依次出队
    #             q.pop()
    #         q.append(i)  # 将当前值加入队列
    #     res.append(nums[q[0]])  # 队首即最大值
    # return res[k - 1:]  # k-1前不是有效的滑动窗口


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = maxSlidingWindow(nums, k)
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

