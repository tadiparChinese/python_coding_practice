import time

while True:
    localtime = time.localtime()

    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, end="", flush=True)
    print("\n", end="", flush=True)
    time.sleep()
