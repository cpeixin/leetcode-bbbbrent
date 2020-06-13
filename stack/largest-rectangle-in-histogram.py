def largestRectangleArea(heights):
    stack = []
    heights = [0] + heights + [0]
    res = 0
    for i in range(len(heights)):
        # print(stack)
        # tmp = stack[-1]
        while stack and heights[stack[-1]] > heights[i]:
            stack_1 = stack[-1]
            tmp = stack.pop()
            res = max(res, (i - stack[-1] - 1) * heights[tmp])
        stack.append(i)
    return res


def largestRectangleArea_1(height):
    # 我们在末尾添加零是因为我们要始终确保当前考虑的高度小于堆栈中存储的高度的条件
    height.append(0)
    # 我们以-1实例化堆栈，作为对添加到height的0的引用
    # 它总是将第一个高度添加到堆栈中，因此它不是空的
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        # 新近元素和栈顶元素笔比较，如果新进元素小于栈顶元素，则栈顶元素出栈。
        while height[i] < height[stack[-1]]: # 这里也就是对应height.append(0)，
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    # height.pop()
    return ans

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    result = largestRectangleArea_1(heights)
    print(result)
