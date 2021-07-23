# using lambdas to create closures

# ===criteria=======
# We must have a nested function (function inside a function). 
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.

def power(x, y):
    return x ** y

square = lambda x: power(x, 2)
cube = lambda x: power(x, 3)

print(square(5))
print(cube(5))