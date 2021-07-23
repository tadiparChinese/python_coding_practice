def missingNumber(arr, num):
    elements_sum = num*(num+1)//2
    return elements_sum - sum(arr)

arr = [1,2,3,4,5,6,8]
num = len(arr)+1
print(missingNumber(arr, num))