list = [1,8,6,2,5,4,8,3,7]

# 左右边界，不重复双重遍历

for i in range(len(list)-1):
    for j in range(1, len(list)):
        print(list[i], list[j])