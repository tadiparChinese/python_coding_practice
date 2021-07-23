#using list comprehension to "add up" two lists element by element
i = 0
data1 = [1, 3, 5, 7]
data2 = [2, 4, 6, 8]

data3 = [data1[i] + data2[i] \
    for i in range(len(data1))]

print(data3)