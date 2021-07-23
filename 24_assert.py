# The "assert" keyword can be used to check the input data for validity.
# If the assert condition is not true,
# the program quits with the "AssertionError" exception (if you did not catch it)

def divide(x,y):
    assert y != 0
    return x/y

a = divide(100, 10) #ok

print(a)

a = divide(100, 0) # not ok
print(a) #will not print 