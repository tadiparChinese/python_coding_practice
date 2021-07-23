# After installing Python, you get not only a compiler but also a set of useful libraries (modules)


#how to rotate the list without 'append' and 'pop'

from collections import deque

data = deque([1,2,3,4,5])

for _ in range(len(data)): #for _ in range(5)
    data.rotate(1)  # or -1
    print(list(data))