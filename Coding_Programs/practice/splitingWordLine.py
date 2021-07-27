fp = open("C:\Users\PRATIK\Desktop\test.txt")
data = fp.read()
# print(data)

lines = data.split("\n")
for line in lines:
    words = line.split(" ")
    for word in words:
        print(word)
    #print(line)
fp.close()
