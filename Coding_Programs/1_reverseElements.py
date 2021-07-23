#reversing the elements in list 

def revList(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end+=1
arr = [3,4,5,6,7,8]
num = len(arr)
revList(arr, 0, num)
print(arr)

#error in program