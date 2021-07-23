#find continious subarray of elements
def subArraySum(arr, num, sum_):
    curr_sum = arr[0]
    start = 0
    i = 1

    while i <= num:
        while curr_sum > sum_ and start < i-1:
            curr_sum = curr_sum - arr[start]
            start+=1

        if curr_sum == sum_:
            print("Sum found between indexes")
            print(start, i-1)
            return 1
        if i < num:
            curr_sum = curr_sum + arr[i]
        i+=1
    print("No subarray found")
    return 0
arr = [1,4,20,3,10,5]
num = len(arr)
sum_ = 33   # 20+3+10 ===> indices 2, 4
subArraySum(arr, num, sum_)