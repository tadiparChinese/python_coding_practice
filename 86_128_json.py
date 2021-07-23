# Dumping a structured variable to a text file in JSON format.
# Notice that the interface of the libry

# saving the data structure in a file in json format
import json

data = {
    "alpha" : [3,5,7],
    "beta" : [4,6,8]
}

with open('data.json', 'w') as f:
    json.dump(data, f)

#using text format now
with open('data.json', 'r') as f:
    restored = json.load(f)
    print(restored)

