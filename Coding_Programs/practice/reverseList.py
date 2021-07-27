#1. reverse()

list1 = [4,7,9,2]
# list1. reverse() #not taking any memory
# print(list1)

# 2. slicing
list2 =list1[::-1] #taking extra memory
# print(list2)

# 3. reversed()
list3 = list(reversed(list1))
#print(list3)


# 4. loop
list4 = []
for i in range(len(list1)-1, -1, -1):
    list4.append(list1[i])
print(list4)

