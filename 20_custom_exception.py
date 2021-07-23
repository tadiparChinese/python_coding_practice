# creating custom exceptions

class ExceptionA(Exception): #inherits
    pass #adds nothing

class ExceptionB(Exception):
    pass

for n in range(6):
    try:
        if n % 2:
            raise ExceptionA
        else:
            raise ExceptionB
    except ExceptionA:
        print('Exception A cought')
    except ExceptionB:
        print('Exception B cought')