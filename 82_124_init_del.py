# create a custom constructor and destructor for class

class C:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('destructor')
    
o = C() #constructor called
print('Hello, World!') #destructor will called at end of program
