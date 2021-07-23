# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting = func("""Hi, I am creating function passed as an argument""")
#     print(greeting)

# greet(shout)
# greet(whisper)
# # print(shout('Hello'))

# # yell = shout

# # print(yell('Hello'))


# def create_adder(x):
#     def adder(x):
#         return x+y
#     return adder

# add_15 = create_adder(15)
# print(add_15(10))


# @gfg_decorator
# def hello_decorator():
#     print('GFG')

# '''Above code is equivalent to

# def hello_decorator():
#     print('GFG')

# hello_decorator = gfg_decorator(hello_decorator) '''



# def hello_decorator(func):
#     def inner1():
#         print('HEllo, this is before function execution')

#     func()
#     print('This is the after function execution')
#     return inner1()

# def function_to_be_used():
#     print('This is inside the function')

# function_to_be_used = hello_decorator(function_to_be_used)

# import time
# import math

# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken in ", func.__name__, end - begin)

#     return inner1


# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
# factorial(10)
 

# def hello(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))
# hello(9)

# def isPrime(n):
#     flag = False
#     if n > 1:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         print(n, "is not a prime number")
#     else:
#         print(n, "is a prime number")
# isPrime(9)


# def cal(n):
#     return n*n
# num = (2,3,4,5,6)
# result = map(cal, num)
# print(result)

my_list = [2,3,4,5,6]
sq_list = [x*x for x in my_list if x%3 == 0]
print(sq_list)