def evenNumbers(n):
    i = 1
    while n:
        yield 2*i
        i+=1
        n-=1

it = evenNumbers(10)
even_list=[]
while True:
    try:
        even_list.append(next(it))
        #even_list+=next(it)
    except StopIteration:
        break

print(even_list)