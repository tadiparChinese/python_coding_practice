sentence1 = "Hi all, my name is Tom...I am orininally form Nagpur"
sentence2 = "I need to work very hard to learn more about algorithms in Python"

#remove the punctuations

def solution(sentence):
    for p in "!?',;:.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/ len(words), 2)

print(solution(sentence1))
print(solution(sentence2))