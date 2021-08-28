class Car:
    base_price = 10000
    def __init__(self, windows, doors, power):
        self.windows = windows
        self.doors = doors
        self.power = power

    def what_base_price(self):
        print('The base price is {}'.format(self.base_price))

    @classmethod
    def revise_base_price(cls, inflation):
        cls.base_price =cls.base_price+cls.base_price*inflation

Car.revise_base_price(0.10) #use this as standard practice
print(Car.base_price)

car1 = Car(4,5,2000)
car1.revise_base_price(0.10)
print(car1.base_price)
