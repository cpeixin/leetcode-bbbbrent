# for i in range(1,2):
#     print(i)


list = [[1], [1, 1], [1, 2, 1]]


print(list[-2][1])



list_2 = [1]+[2]
print(list_2)



a = [list[-1][i-1]+list[-1][i] for i in range(1, 4 - 1)]

print(a)

print(list[-1])