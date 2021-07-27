def fib_Gen():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = c+a
        yield c

f = fib_Gen()
for i in range(20):
    print(next(f), end=" ")