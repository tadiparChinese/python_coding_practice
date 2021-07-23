#creating simple documentation

def my_f(x):
    '''this function returns a double value of its argument'''
    return x * 2
print(my_f(5))

#print the doc:
print(my_f.__doc__)