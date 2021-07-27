dict1 = {1:'apple', 2: 'banana'}
dict2 = {3: 'orange', 4: 'kiwi'}

# dict1.update(dict2) # update never return new list. It will modify existing list.
# print(dict1)

dict3 = {**dict1, **dict2}
print(dict3)