try:
    a = int(input('Enter the number 1: '))
    b = int(input('Enter the number 2: '))
    c = a/b

except NameError:
    print('The user have not defined the variable')
    
except ZeroDivisionError:
    print('Please provide number greater than zero')
    
except TypeError:
    print('Try to make datatypes similar')
    
except Exception as ex:
    print(ex)

else:
    print(c)
finally:
    print('The execution is done')