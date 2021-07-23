# def twoSum(arr, sum):
#     while (0 < sum):
#         for i in range(0, len(arr)-1):
#             for j in range(1, len(arr)):
#                 if arr[i] + arr[j] == sum:
#                     return(arr[i], arr[j])

# arr = [2,7,11,15]
# sum = 26
# print(twoSum(arr, sum))



#======anather method=============

# def twoSum(arr, sum):
#     arr.sort()
#     left = 0
#     right = len(arr)-1
#     while(left <= right):
#         if(arr[left] + arr[right]>sum):
#             right=right-1

#         elif(arr[left] + arr[right]<sum):
#             left=left+1
        
#         elif(arr[left] + arr[right]==sum):
#             print("Values of pair are", arr[left], "&", arr[right])
#             right=right-1
#             left=left+1
    

def twosum_hashmap(arr, sum):
    dict = {}
    for i in range(len(arr)):
        if(sum - arr[i] in dict):
            return [sum-arr[i], arr[i]]
        elif(arr[i] not in dict):
            dict[arr[i]]=i


arr = [5,7,4,3,9,8,19,21]
sum = 17
s = twosum_hashmap(arr, sum)
print(s)

