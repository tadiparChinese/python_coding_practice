def freq_words():
    str = input("Enter the string: ")
    li = str.split()

    dic = {}
    for i in li:
        if i not in dic.keys():
            dic[i] = 0
        dic[i] = dic[i] + 1
    print(dic)

freq_words()