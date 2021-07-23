# The "zip" built-in function takes a few lists (two in this example), 
# and creates tuples by picking up elements from each list.
# The first tuple contains elements from the first positions in the lists, and so on.

colors = ['red', 'green', 'yellow']
fruits = ['apple', 'peer', 'banana']

z = zip(colors, fruits)
for x in z:
    # x is a tuple
    print(x[0] + ' : ' + x[1])