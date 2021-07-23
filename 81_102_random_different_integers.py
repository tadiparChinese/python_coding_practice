# generating a series of *different* random numbers

from random import randint

data = set()
while len(data) < 20:
    r =  randint(0, 100)
    data.add(r) #new or existing numbers

print(len(data)) #got 20 items
print(data) #all different
