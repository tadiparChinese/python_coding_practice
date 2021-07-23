# The pair of built-in functions,
# "all" and "any" will check if the elements of the list are either


# test if all or any
# items are True

data = [True, True, False]

if any(data):
    print('Some are True')
else:
    print('Not a single True')

if all(data):
    print('All are True')
else:
    print('Not all True')