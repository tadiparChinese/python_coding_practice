#you cannot directly access or modify a global variable that is outside of your local scope

n = 1 
def inc_n():
    # will show error if not define n = global
    global n # hence defining n as global
    n+=1

print(n)
inc_n()
print(n)