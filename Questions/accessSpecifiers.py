# there is no such thing called access specifiers in python, but for programer's convinience we wrote it
#nobody will restrinct you from overriding but it's just an hint to the developer

# protected : _ (only child class i.e. subclass can access the variables)
# private: __ (only current class can access the variables)


# protected: only child class can access the data
class Car:
    def __init__(self, windows, doors, enginetype):
        self._windows = windows
        self._doors = doors
        self._enginetype = enginetype
    def drive(self):
        print('I can drive')

class Truck(Car):
    def __init__(self, windows, doors, enginetype, horsepower):
        super().__init__(windows, doors, enginetype)
        self.horsepower = horsepower



#private: variables are not accessed or modified outside of class
#### would call it 'name mangling' next time instead of calling it private
class Car1:
    def __init__(self, windows, doors, enginetype):
        self.__windows = windows
        self.__doors = doors
        self.__enginetype = enginetype
    def drive(self):
        print('I can drive')

car1 = Car1(4,4,'diesel')
print(dir(car1))