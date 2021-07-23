# Saving an if condition in a temporary boolean variable

max = 100
x = 200

ok = x < max
print(type(ok))

if ok:
    print('OK')
else:
    print('Not OK')

    #<class 'bool'>
    # Not OK