# to iterate backwards in python, either use a range with step = -1, or a "reversed" built-in function

#going along a list backwards

my_list = ['alpha', 'beta', 'gamma']

#method 1
for x in my_list[::-1]: # -1 is for reverse order
    print(x)

print('---after---')
#method 2
for y in reversed(my_list):
    print(y)