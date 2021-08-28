class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
        
    def drive(self):
        print('I can drive the car')
        
class Audi(Car):
    def __init__(self, windows, doors, enginetype, enableai):
        super().__init__(windows, doors, enginetype)
        self.enableai = enableai
        
    def selfdriving(self):
        print("I can selfdrive")
audi = Audi(5,6,'diesel', True)
print(dir(audi))
print(audi.enableai)
print(audi.drive())
print(audi.selfdriving())