#object reference to new object

class Test:
    def __init__(self,x):
        self.x = x
    
    def get_data(self):
        print("some code to fetch data from database")

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()
    
t1 = Test(5)
t1.f1()
t1.f2()

def new_get_data(self):
    print('some code to fetch data from test data')

Test.get_data = new_get_data
print('after monkey patching')
t1.f1() #some code to fetch data from test data
t1.f2() #some code to fetch data from test data