# In Python "pickle" module, you can freeze your data objects to a file, 
# and later read them back.

# but don't use pickle as it can result in code execution 
# if someone has access to this file Or only unpickle things you trust

#saving the datastructure in a file

import pickle

data = {
    "alpha": [3,5,7],
    "beta": [4,6,8]
}

with open('data.bin', 'wb') as f:
    pickle.dump(data, f)

with open('data.bin', 'rb') as f:
    restored = pickle.load(f)
    print(restored)