# To split a string into characters, convert it to a list,
#  and you'll get a list of separate characters.
# Of course, you can access individual characters directly by indexing a string.


my_str = 'hello this is my name'
#first, print a charecter
print(my_str[3])

#now, make a list out of a string by converting it in type:

chars = list(my_str)
print(type(chars))
print(chars[3])
#spliting the string in words
str = my_str.split(' ')
for i in str:
    print(i)