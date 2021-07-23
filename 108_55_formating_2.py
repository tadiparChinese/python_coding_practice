# You can use indices inside {} to indicate which argument of the format method to substitute at this place

a, b = 10, 20

print('a + b = b + a')
print('{0} + {1} = {1} + {0}'.format(a,b))

#{0} replaced with a
#{1} replaced with b
# but you only mention them once
