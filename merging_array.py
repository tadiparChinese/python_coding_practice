def mergeArray(a, b, l1, l2):
    arr = [None] * (l1+l2)
    a = sorted(a)
    b = sorted(b)
    i = j = k = 0
    while i < l1 and j < l2:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
    while i < l1:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < l2:
        arr[k] = b[j]
        j+=1
        k+=1
    print('Array after merging: ')
    for i in range(l1+l2):
        print((arr[i]), end=" ")
        # still need to remove duplicate entries please work on it

# driver program

a = [2,34,53,23,45,52,6,3,7,8,21]
l1 = len(a)
b = [3,4,52,6,4,74,73,78,45]
l2 = len(b)

mergeArray(a,b,l1,l2)


