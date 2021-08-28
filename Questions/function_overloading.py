#python  does not support function overloading, here in python functions are acted like objects , it act as reference variable which contains the function object's id
#only supports first class functions

def f1():
    print('First function')

def f1(a,b):
    print('Second function')

f1()
f1(3,4) #error dega coz it only take second function as function (baad me banaya wala)if you dont provide arguments
# TypeError: f1() missing 2 required positional arguments: 'a' and 'b'