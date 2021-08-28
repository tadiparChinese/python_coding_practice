# 1. function copy

def welcome():
    return "Welcome to the Python"

wel = welcome()
#print(wel)
del welcome
#print(wel) # delete nahi hoga coz yaha pe function copy hua hai but if you call welcome() then it will show error
# welcome() # shows error message NameError: name 'welcome' is not defined

# 2. closures
#function inside function: what ever parameters are passed to main function it would be accessable to child function

def main_welcome(func):
    def sub_welcome():
        print('welcome to the Python')
        func('hope you are doing well')
        print('good morning')
    return sub_welcome()
main_welcome(print)

#example
def outer_func(func):
    def inner_func():
        print('how are you')
        print(func([1,2,3,4,5,6,7,8,9,10,11]))
        print('I am fine')
    return inner_func()
outer_func(len)

  
# 3.decorators
def main1(func):
    def sub_main():
        print('ramesh')
        func()
        print('suresh')
    return sub_main()

@main1  # same as a=main1(main2)
def main2():
    print('THis is main2')

# eg: in django we have @app.route