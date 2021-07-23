# When a function returns more than one value
def f():
    return 10, 11

a, b = f()
print(a)
print(b)

# if you only take one 

c = f()
print(c) # (10, 11) you take a tuple, not a single value