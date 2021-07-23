# reading from the text file

for str in open('t.txt'):
    # print(str) # we should not print the newline after each string as "str" already contains it

    print(str, end='')