# in Python, you can operate with embedded lists. 
# Specify as many indices as needed to get to the depth of the element


# multi-diamention array

my_list = [
    [1,3,5],
    [7,9,11],
    [13,15,17]
]

print(my_list[1]) # [7,9,11]
print(my_list[1][2]) # [11]
















# Matrices are only 2-dimensional. Tensors are what you're thinking about - 
# it includes numbers, vectors (1d array), maricies (2d array) and all the other variants. 
# Also, python can have lists like [[1,2],[3]] where each of the 'sublists' have different lengths, 
# which isn't possible in a matrix/tensor.