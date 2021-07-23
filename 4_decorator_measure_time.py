# using decorator to measure time
import time

def time_measure(f): # f =function here
    t0 = time.time()
    f()  #call that function
    t = time.time()
    return t - t0

@time_measure #decorator
def slow_time():
    time.sleep(2)

print(slow_time) # no () function called only 