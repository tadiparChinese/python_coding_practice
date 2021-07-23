# try - finally
# try - except
# try - except - finally 
# try - except - else
# try - except - else - finally

def f():
    try:
        print(1/0)
    except:
        print('Exception')
        return 0
    finally:
        print('Finally')
        #the finally block will work here
    print('Return') #will not be printed
    return 1
print('start')
f()
print('Finish')