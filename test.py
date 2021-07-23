class A:
    @staticmethod
    def func1():
        pass


    #creating alternating inheritable constructors
    @classmethod
    def func(cls):
        pass

# Gloabal Interpreter Lock for concurrency

def func3(x: int, y: str) -> bool:
    return False


# generator
def range(start, end, step):
    cur = start
    while cur > end:
        yield cur
        cur += step
range(1,11,2)