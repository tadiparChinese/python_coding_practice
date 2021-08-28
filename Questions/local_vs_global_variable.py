# x = 5 #global
# def f1():
#     y = 10 #local
#     print(f'x = {x}, y= {y}')
# f1()
# print(x,y) #y will give error


# x = 5
# def f1():
#     global x
#     x=10
#     print(f'x={x}')
# f1()
# print(x)

x=5
def f1():
    x = 4
    d = globals() #return a global variable dictionary and gives as a string 
    d['x'] = 10 #gives back the string denote to global variable x
    print("local x=%d  global x=%d "%(x, d['x']))
f1()
print(x)