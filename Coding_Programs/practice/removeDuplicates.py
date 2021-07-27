arr = [1,4,2,5,2,3,4,1,4,5,2,3]

#using set
# arr2 = list(set(arr))
# print(arr2)



#using empty array

# arr3 = []
# for i in arr:
#     if i not in arr3:
#         arr3.append(i)
# print(arr3)



#using lambda function
# rem_dupLicate_func = lambda arr:set(arr)
# print(rem_dupLicate_func(arr))

#using dictinary

dict1 = {
    'cars':["Ford", "Toyota","Ford", "Toyota"],
    'brand':["Mustang", "Ranz","Mustang", "Ranz"]
}

dict2 ={}
for key, value in dict1.items():
    dict2[key]=set(value)
#print(dict2)


# as symetric difference remove duplicate elements
set1 = {1,2,4,5}
set2 = {2,1,5,7}
rem_dup_ele = set1.symmetric_difference(set2)
print(rem_dup_ele)



