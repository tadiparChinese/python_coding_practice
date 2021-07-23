from mylib import f
# using the function from mylib
print(f(5)) #10

#defining a local function
def f(x):
    #with different behaviour
    return 3 * x

# same code as before
print(f(5)) #15
#but different result