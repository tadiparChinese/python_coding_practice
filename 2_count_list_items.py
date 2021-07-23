#count how many times each item appears in the list

my_list = [
    'a', 'b', 'a', 'b', 'c', 'b', 'd', 'b', 'e', 'f'
]

for item in sorted(set(my_list)):
    #use set otherwise it will print b value 4 times
    count = my_list.count(item)
    print(f'{item} = {count} times')