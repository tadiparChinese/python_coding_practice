# In Python, you can raise the "StopIteration" exception when you want the next call of "next" to fail
# creating custom iterators
class C:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        #let's stop when n = 3
        if self.n == 3:
            raise StopIteration
        self.n += 1
        return self.n
c = C()
i = iter(c) # get an iterator
for _ in range(5):
    try: #use the iterator
        print(next(i)
    except:
        break