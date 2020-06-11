import sys
heights = [2,1,5,6,2,3]

for i in range(len(heights)-1):
    min_height = sys.maxsize
    for j in range(i+1, len(heights)):
        # print(heights[i], heights[j])
        min_height = min(heights[j], min_height, heights[i])

    print(i, min_height)


