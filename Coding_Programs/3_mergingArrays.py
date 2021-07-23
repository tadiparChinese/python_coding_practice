def mergeArray(arr1, arr2, n1, n2):
    arr3 = [None] * (n1+n2)
    i =0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k+=1
            i+=1
        else:
            arr3[k] = arr2[j]
            k+=1
            j+=1
    while i < n1:
        arr1[i] < arr2[j]
        k+=1
        i+=1
    while j < n2:
        arr3[k] = arr2[j]
        k+=1
        j+=1
    print("Array after merging: ")
    for i in range(n1+n2):
        print(str(arr3[i]), end=" ")


arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
n1 = len(arr1)
n2 = len(arr2)
mergeArray(arr1, arr2, n1, n2)