#static variables wo hote hai jinko class object ke andar memory milti hai
class Item:
    a = 5
    def __init__(self):
        self.x = 10 #instance object variable
        y = 4 #local variable
        Item.b = 6 #static variable

    def f1(self):
        Item.c=7 #static variable

    @staticmethod
    def f2():
        Item.d=8 #static variable

    @classmethod
    def f3(cls):
        cls.e=9 #static variable
        Item.f=10 #static variable

Item.g=11
