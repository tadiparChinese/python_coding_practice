# Zero number or an empty string are treated as False in boolean context

x = 0
if x:
    print('True')
else:
    print('False')

x = ''
if x:
    print('True')
else:
    print('False')