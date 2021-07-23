# reversed() vs .reverse()

a = ['alpha', 'beta', 'gamma']
b = reversed(a)
print(a) # original a # ['alpha', 'beta', 'gamma']

c = a.reverse()

print(a) # original a is broken # ['gamma', 'beta', 'alpha']


# note1: It is not broken. And your c is None. 
# list.reverse() is an inplace method that will reverse original list. It will not return new list. It will modify existing list. 
# The same as calling list.append(x) will add x to the list. It will NOT return new list. It will modify existing list.
# Stop saying something is broken when it clearly not!

# note2: There's a difference between [::-1] and .reverse(), .reverse() is in-place, it modifies the list, while [::-1] returns a new list, kinda like reversed but it's a list and not an iterator.