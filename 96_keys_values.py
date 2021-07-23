# getting keys and values of dictionary

data = {
    "France" : "Paris",
    "India" : "New Delhi",
    "Italy" : "Rome"
}
print(data.keys())
print(data.values())

#iteration
for key, value in data.items():
    print(key, value)