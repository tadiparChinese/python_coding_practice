# Lists in Python can be used as a stack:
# you add data to the end of the list using the "append" methd

# push and pop in list

data = []
for i in range(5):
    data.append(i * i)
    # fill with some data
while(len(data)):
    #while list is not empty
    value = data.pop()
    print(value)
    #printed in reverse order