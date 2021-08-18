def freqCount(str1):
    # make dictionary of it not list
    res = {i : str1.count(i) for i in set(str1)}
    return res

str1 = "hellohowareyou"
print(freqCount(str1))

