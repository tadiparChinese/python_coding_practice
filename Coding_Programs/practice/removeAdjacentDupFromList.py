def removeDups(L):
    if len(L) <= 1:
        return L
    return [L[i] for i in range(len(L)) if i==0 or L[i-1] != L[i]]


L= [10,20,20,20,20,20,30,40,40,50,]
print(removeDups(L))