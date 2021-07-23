# You can pass named arguments when calling the "format" method on a string. 
# Give the temporary names to your placeholders and usem them directly in curly braces.


#what is the use of "\" ?

#Whenever u wanna bring a raw on a new line u should use "\" in python to make it work, 
# otherwise it will throw an error 

first_name = 'James'
last_name = 'Bond'

greeting = \
    'My name is {last}. {first} {last}.'.format(
        first = first_name,
        last = last_name
    )

print(greeting)