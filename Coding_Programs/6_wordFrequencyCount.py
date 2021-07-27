def freqCount(str1):
    res = {i : str1.count(i) for i in set(str1)}
    return res

str1 = "hellohowareyou"
print(freqCount(str1))

