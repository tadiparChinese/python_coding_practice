# Friend that is what should happen and in every language it is like that, 
# if a variable has a value other than 0 it is true, 
# however in a string all the elements are characters 
# and the character '0' in its integer value is 48 therefore it is different from 0 
# and that is why it is true and it will be like this for any character or value other than 0


# a string that contains zero is still True in boolean context

s = '0'

if s:
    print(True)
else:
    print(False)