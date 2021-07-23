#using iterators

my_list = ["alpha","beta", "gamma"]

#make the list iterable
data = iter(my_list)

a = next(data)
print(a)

a = next(data)
print(a)

a = next(data)
print(a)
