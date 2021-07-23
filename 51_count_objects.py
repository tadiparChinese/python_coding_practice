# ye galat program likha hai: 
# You had to write the class name "Item" twice in your code, 
# that means that if you ever wanted to change the name of the class 
# you would need to go hunt everywhere it's mentioned. Instead,use type(self) or self.__class__.
# Another note is the method you defined in the class, 
# it's pointless, you can just access the attribute directly, you don't need a getter.

# counting objects

class Item:
    counter = 0
    
    def __init__(self):
        Item.counter += 1
        self.counter = Item.counter

    def my_number(self):
        return self.counter

for _ in range(5):
    objectN = Item()
    print('My number is ' + str(objectN.my_number()))