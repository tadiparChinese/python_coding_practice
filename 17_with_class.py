# demonstrating the work of the __enter__and __exit__ methods 
# using 'with' we can use the resources

class C:
    def some_work(self):
        print('Hello, there')
    #1
    def __enter__(self):
        print('ENTER')
    def __exit__(self, a1, a2, a3):
        print('EXIT')
o = C()

with o:
    #as soon as you have "with", you need __enter__ and __exit__
    o.some_work()