# Python any other class, custom exception can define a constructor and you can pass arguments

class MyException(Exception):
    def __init__(self, message):
        print(message)

#now use it

try:
    raise MyException('SOS!')
except:
    print('Caught')







# In python they are not called "constructors", they are called "initializers" or "__init__" in short.