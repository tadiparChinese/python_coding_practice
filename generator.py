#convert list into string

# weekdays = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat']
# listTuple = tuple(weekdays)
# listString1 = ' '.join(weekdays)
# print(listString1)
# print(listTuple)


#count the occurence of perticular element in list
# example 1
# weekdays = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat']
# print(weekdays.count('mon'))


# example 2
# weekdays = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat']
# print([[x, weekdays.count(x)] for x in set(weekdays)])


#enumerator

subjects = ('Python', 'Interview', 'Questions')

for i, subject in enumerate(subjects):
    print(i, subject)