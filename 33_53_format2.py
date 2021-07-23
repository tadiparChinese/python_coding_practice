# Use more than one placeholder in a string if you need to interpolate more than one variable. 
# Prefer the style you like the most. 
# C programmers are familiar with the %s syntax from the well-known printf function. 
# But you may also use the OOP style and call the format method on a string.

name1, name2 = 'John', 'Karla'

# old style
print('Hello, %s and %s!' % (name1, name2))

#new style
print('Hello, {} and {}!'.format(name1, name2))