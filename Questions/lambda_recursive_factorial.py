#if you want to call function only single time then use lambda function
f = lambda n: 1 if n==0 else n*f(n-1)
print(f(5))

print((lambda a,b:a+b)(3,4))