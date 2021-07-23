# Opening, writing to, 
# and closing a text file in Python.
#  Use the "open" built-in function and pass

f = open('t.txt', 'w')

# or:
#f = open('t.txt', mode='w')
#w = create and write
#r = read(default)
#a = append
#x = create if not existed

f.write('Hello, World!')
f.close()





# this is not good form. use "with open(file) as (name):" so you don't have to close it