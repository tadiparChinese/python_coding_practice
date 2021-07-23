# add annotations to the arguments and to the return value of function

# def power(a, b):
#     return a**b

def power(a:int, b:int) -> int:
    return a ** b

#function takes two "int"s and returns an "int"

print(power(2,3))
print(power.__annotations__)